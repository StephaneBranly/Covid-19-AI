# import libraries
import pydotplus
from sklearn.externals.six import StringIO
import urllib.request
import numpy as np
from sklearn import linear_model
import sys
from bs4 import BeautifulSoup
from pathlib import Path

import requests

print("\033[0;37;41m#####      Covid-19-AI      #####")
print("")
print("By @stephane_branly")
print("https://github.com/StephaneBranly")
print("Python 3.6.2")
print("")
print("\033[0;37;41m#####                       #####")
print("\033[0;37;48m")

download = input("Do you want to download data (y/n) ? ")
if(download == "y"):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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

            if(soup != ""):
                data_current_file = str(soup)
                data_current_file = data_current_file.replace("\r", "")
                data_current_file = data_current_file.split("\n")
                for i in range(1, len(data_current_file)):
                    data_current_line = data_current_file[i]
                    data_current_line = data_current_line.replace(
                        "Boston, MA", "Boston MA")
                    data_current_line = data_current_line.replace(
                        "Berkeley, CA", "Berkeley CA")
                    data_current_line = data_current_line.replace(
                        "Madison, WI", "Madison WI")
                    data_current_line = data_current_line.replace(
                        "New York City, NY", "New York City NY")
                    data_current_line = data_current_line.replace(
                        "Norfolk County, MA", "Norfolk County MA")
                    data_current_line = data_current_line.replace(
                        "Tempe, AZ", "Tempe AZ")
                    data_current_line = data_current_line.replace(
                        "Humboldt County, CA", "Humboldt County CA")
                    data_current_line = data_current_line.replace(
                        "Los Angeles, CA", "Los Angeles CA")
                    data_current_line = data_current_line.replace(
                        "Maricopa County, AZ", "Maricopa County AZ")
                    data_current_line = data_current_line.replace(
                        "Orange, CA", "Orange CA")
                    data_current_line = data_current_line.replace(
                        "San Antonio, TX", "San Antonio TX")
                    data_current_line = data_current_line.replace(
                        "Placer County, CA", "Placer County CA")
                    data_current_line = data_current_line.replace(
                        "Sarasota, FL", "Sarasota FL")
                    data_current_line = data_current_line.replace(
                        "Sonoma County, CA", "Sonoma County CA")
                    data_current_line = data_current_line.replace(
                        "Umatilla, OR", "Umatilla OR")
                    data_current_line = data_current_line.replace(
                        "Wake County NC", "Wake County NC")
                    data_current_line = data_current_line.replace(
                        "Westchester County, NY", "Westchester County NY")
                    data_current_line = data_current_line.replace(
                        "Lackland, TX", "Lackland TX")
                    data_current_line = data_current_line.replace(
                        "Omaha, NE", "Omaha NE")
                    data_current_line = data_current_line.replace(
                        "Travis, CA", "Travis CA")
                    data_current_line = data_current_line.replace(
                        "Travis, CA", "Travis CA")
                    data_current_line = data_current_line.replace(
                        "Santa Clara, CA", "Santa Clara CA")
                    data_current_line = data_current_line.replace(
                        "Seattle, WA", "Seattle WA")
                    data_current_line = data_current_line.replace(
                        "Chicago, IL", "Chicago IL")
                    data_current_line = data_current_line.replace(
                        "San Benito, CA", "San Benito CA")
                    data_current_line = data_current_line.replace(
                        "Toronto, ON", "Toronto ON")
                    data_current_line = data_current_line.replace(
                        "London, ON", "London ON")
                    data_current_line = data_current_line.replace(
                        "San Diego County, CA", "San Diego County CA")
                    data_current_line = data_current_line.replace(
                        "Sacramento County, CA", "Sacramento County CA")
                    data_current_line = data_current_line.replace(
                        "Montreal, QC", "Montreal QC")
                    data_current_line = data_current_line.replace(
                        "Snohomish County, WA", "Snohomish County WA")
                    data_current_line = data_current_line.replace(
                        "Portland, OR", "Portland OR")
                    data_current_line = data_current_line.replace(
                        "Providence, RI", "Providence RI")
                    data_current_line = data_current_line.replace(
                        "King County, WA", "King County WA")
                    data_current_line = data_current_line.replace(
                        "Cook County, IL", "Cook County IL")
                    data_current_line = data_current_line.replace(
                        "Grafton County, NH", "Grafton County NH")
                    data_current_line = data_current_line.replace(
                        "Hillsborough, FL", "Hillsborough FL")
                    data_current_line = data_current_line.replace(
                        "San Mateo, CA", "San Mateo CA")
                    data_current_line = data_current_line.replace(
                        "Fulton County, GA", "Fulton County GA")
                    data_current_line = data_current_line.replace(
                        "Washington County, OR", "Washington County OR")
                    data_current_line = data_current_line.replace(
                        "Wake County, NC", "Wake County NC")
                    data_current_line = data_current_line.replace(
                        "Orange County, CA", "Orange County CA")
                    data_current_line = data_current_line.replace(
                        "Contra Costa County, CA", "Contra Costa County CA")
                    data_current_line = data_current_line.replace(
                        "Ashland, NE", "Ashland NE")
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

    fichier = open("datas2.csv", "w")
    for i in range(0, len(data_table)):
        for j in range(0, len(data_table[i])):
            data_table[i][j] = str(data_table[i][j])
            if(data_table[i][j] == ""):
                data_table[i][j] = "0"

        while(len(data_table[i]) != 8):
            data_table[i].append("0")
        data_table[i][2] = data_table[i][2].replace("-", "")
        data_table[i][2] = data_table[i][2].replace("T", "")
        data_table[i][2] = data_table[i][2].replace(" ", "")
        data_table[i][2] = data_table[i][2].replace("/", "")
        data_table[i][2] = data_table[i][2].replace(":", "")
        data_table[i][0] = '0'
        data_table[i][1] = '0'
        fichier.write(",".join(data_table[i])+"\n")
    fichier.close()

    print("\033[0;37;41m# Downloading finished")
print("\033[0;37;48m")
print("\033[0;37;41m# Starting AI")
print("\033[0;37;48m")


f = open("datas.csv")
titan = np.loadtxt(f, delimiter=',', skiprows=1)

nombre_test = 20
test_idx = []
fin_titan = len(titan)-1
for i in range(0, nombre_test):
    test_idx.append(fin_titan-(1*i))
fin_titan = len(titan)-1

target = titan[:, [3, 4, 5]]
data = titan[:, [2, 6, 7]]

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
