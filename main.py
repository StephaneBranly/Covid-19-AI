# import libraries
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import urllib.request
import numpy as np
from sklearn import linear_model
import sys
from bs4 import BeautifulSoup
from pathlib import Path
import re
import requests

print("\033[0;37;41m#####      Covid-19-AI      #####")
print("")
print("By @stephane_branly")
print("https://github.com/StephaneBranly")
print("Python 3.6.2")
print("")
print("\033[0;37;41m#####                       #####")
print("\033[0;37;48m")

month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

download = input("Do you want to download data (y/n) ? ")
if(download == "y"):
    date_start = '01-22-2020'
    date_end = input("Write the end data date (day included)(mm-dd-yyyy) : ")

    print()
    print("\033[0;37;41m# Downloading data from github")
    print("\033[0;37;48m")
    print()

    date_start = date_start.split('-')
    date_end = date_end.split('-')

    data_table = []
    data_current_file = []
    data_current_line = []

    is_last_file = False

    for m in range(1, int(date_end[0])+1):
        if (m == int(date_end[0])):
            day_end = int(date_end[1])
        else:
            day_end = month_days[m-1]

        if(m == 1):
            day_start = int(date_start[1])
        else:
            day_start = 1
        for d in range(day_start, day_end+1):
            # specify the url
            quote_page = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{:02d}-{:02d}-2020.csv".format(
                m, d)
            print(quote_page)
            # query the website and return the html to the variable ‘page’
            page = urllib.request.urlopen(quote_page)
            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(page, 'html.parser')

            if(d == day_end and m == int(date_end[0])):
                is_last_file = True
                last_file_size= len(data_current_file)
            if(soup != ""):
                data_current_file = str(soup)
                data_current_file = data_current_file.replace("\r", "")
                data_current_file = data_current_file.split("\n")
                for i in range(1, len(data_current_file)):
                    data_current_line = data_current_file[i]
                    #for city in city_list:
                    #    data_current_line = ''.join(data_current_line).replace(city, city.replace(",",""))
                    match1 = re.match(r'([a-zA-Z0-9_()",.\s]+)(,US|, US|,Canada|, Canada)',''.join(data_current_line))
                    if match1:
                        data_current_line=''.join(data_current_line).replace(str(match1.group(1)), str(match1.group(1)).replace(", ",""))
                    data_current_line = data_current_line.replace("Korea, South","Korea South")
                    data_current_line = data_current_line.replace("Gambia, The","Gambia The")
                    data_current_line = data_current_line.replace("Bahamas, The","Bahamas The")
                    data_current_line = data_current_line.split(',')
                    if(data_current_line != [""]):
                        data_table.append(data_current_line)

                        if(is_last_file == True):
                            for l in range(0, len(data_table)-1):
                                if(data_table[l][0] == data_current_line[0] and data_table[l][1] == data_current_line[1]):
                                    if(len(data_table[l]) == len(data_current_line)):
                                        data_table[l][6] = data_current_line[6]
                                        data_table[l][7] = data_current_line[7]
                                    else:
                                        data_table[l].append(
                                            data_current_line[6])
                                        data_table[l].append(
                                            data_current_line[7])
        print("")

    fichier = open("datas.csv", "w")
    for i in range(0, len(data_table)):
        for j in range(0, len(data_table[i])):
            data_table[i][j] = str(data_table[i][j])
            if(data_table[i][j] == ""):
                data_table[i][j] = "0"

        while(len(data_table[i]) != 8):
            data_table[i].append("0")
        date=str(data_table[i][2])
        match1 = re.search(r'(\d+/\d+/\d+)',date)
        match2 = re.search(r'(\d+-\d+-\d+)',date)
        if match1:
            match1=match1.group(1).split("/")
            day=int(match1[1])
            month=int(match1[0])
        elif match2:
            match2= match2.group(1).split("-")
            day=int(match2[2])
            month=int(match2[1])
        else:
            print("Pas de match pour i ="+str(i))
            day=1
            month=1
        timestamp = 0
        for m in range(0, int(month)):
            if(m+1 == int(month)):
                timestamp = timestamp+int(day)*60*60*24
            else:
                timestamp = timestamp+month_days[m]*60*60*24
        data_table[i][2] = str(timestamp)
        data_table[i][0] = "\""+data_table[i][0].replace("\"","")+"\""
        data_table[i][1] = "\""+data_table[i][1].replace("\"","")+"\""
        #data_table[i][0] = 0
        #data_table[i][1] = 0
        fichier.write(",".join(data_table[i])+"\n")
    fichier.close()

    print("\033[0;37;41m# Downloading finished")
    print("\033[0;37;48m")
    print("\033[0;37;41m# Dividing in multiple files")
    print("\033[0;37;48m")
    i=len(data_table)-1
    last_timestamp=data_table[i][2]
    while(i>0 and i>= len(data_table)-2-last_file_size):
        city_file_name="places"+"/"+str(data_table[i][0]).replace("\"","")+"_"+str(data_table[i][1]).replace("\"","")
        city_file_name=city_file_name.replace("*","")
        city_file_name=city_file_name.replace(" ","_")
        fichier = open(city_file_name+".csv", "w")
        for j in range(0,i+1):
            if(data_table[j][0] == data_table[i][0] and data_table[j][1] == data_table[i][1]):
                data_table[j][0] = "0"
                data_table[j][1] = "0"
                fichier.write(",".join(data_table[j])+"\n")
        fichier.close()
        i=i-1


print("\033[0;37;48m")
print("\033[0;37;41m# Starting AI")
print("\033[0;37;48m")
#place = input("Write place's name   ")
place1 = "France_France"
place2 = "0_Italy"
place3 = "0_Spain"

f_place1 = open("places/"+place1+".csv")
f_place2 = open("places/"+place2+".csv")
f_place3 = open("places/"+place3+".csv")
f_int = open("datas.csv")
place1_tab = np.loadtxt(f_place1, delimiter=',', skiprows=0)
place2_tab = np.loadtxt(f_place2, delimiter=',', skiprows=0)
place3_tab = np.loadtxt(f_place3, delimiter=',', skiprows=0)
titan = np.loadtxt(f_int, delimiter=',', skiprows=0, usecols=[2,3,4,5,6,7])

nombre_test = 20
test_idx = []
fin_titan = len(titan)-1
for i in range(0, nombre_test):
    test_idx.append(fin_titan-(1*i))
fin_titan = len(titan)-1

target = titan[:, [1, 2, 3]]
data = titan[:, [0, 4, 5]]

if 0:
    # on retire les donnees qu'on veut tester
    train_target = np.delete(target, test_idx, axis=0)
    train_data = np.delete(data, test_idx, axis=0)

    # testing data
    test_target = target[test_idx]
    test_data = data[test_idx]

    # train datas
    n_alphas = 20
    alphas = np.logspace(0, 10, n_alphas)

    coefs = []
    for a in alphas:
        ridge = linear_model.Ridge(alpha=a, fit_intercept=False, solver="auto")
        ridge.fit(train_data, train_target)
        coefs.append(ridge.coef_)

    print("Regression : ")
    print("")
    result = ridge.predict(test_data)
    for x in range(0, len(test_target)):
        print("\033[0;37;42m Real : "+str(test_target[x]) +
            "   |  \033[0;37;41m AI : "+str(result[x]))

    prediction = [0, 0, 0]
    for i in range(0, nombre_test):
        for x in range(0, 3):
            prediction[x] = prediction[x]+(abs(result[i][x]-test_target[i][x]))
    print("\033[0;37;48m")
    print("Error size")
    for x in range(0, 3):
        print((prediction[x]/(nombre_test*3)))


labels = ["Contaminé ", "Morts", "Guéris"]



fig = plt.figure(constrained_layout=True)

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1:, 0])
ax3 = fig.add_subplot(gs[1:, 1])
ax4 = fig.add_subplot(gs[1:, 2])


titan[:,1]=np.log(titan[:,1])

ax1.scatter(titan[:,5], titan[:,4], c=titan[:,1], s=titan[:,1], alpha=0.5)

ax1.set_xlabel(r'longitude', fontsize=9)
ax1.set_ylabel(r'latitude', fontsize=9)
ax1.set_title('planisphere')
ax1.set_xlim(-180,180)
ax1.set_ylim(-90,90)
ax1.grid(True)

ax2.plot(place1_tab[:,2], place1_tab[:,3], label='Contaminés')
ax2.plot(place1_tab[:,2], place1_tab[:,4], label='Morts')
ax2.plot(place1_tab[:,2], place1_tab[:,5], label='Guéris')
ax2.set_xlabel(r'temps', fontsize=9)
ax2.set_title(place1)
ax2.set_ylim(0,100000)
ax2.legend()

ax3.plot(place2_tab[:,2], place2_tab[:,3], label='Contaminés')
ax3.plot(place2_tab[:,2], place2_tab[:,4], label='Morts')
ax3.plot(place2_tab[:,2], place2_tab[:,5], label='Guéris')
ax3.set_xlabel(r'temps', fontsize=9)
ax3.set_title(place2)
ax3.set_ylim(0,100000)
ax3.legend()

ax4.plot(place3_tab[:,2], place3_tab[:,3], label='Contaminés')
ax4.plot(place3_tab[:,2], place3_tab[:,4], label='Morts')
ax4.plot(place3_tab[:,2], place3_tab[:,5], label='Guéris')
ax4.set_xlabel(r'temps', fontsize=9)
ax4.set_title(place3)
ax4.set_ylim(0,100000)
ax4.legend()

fig.suptitle("Covid-19-AI")

plt.show()

