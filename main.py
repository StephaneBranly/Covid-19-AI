# import libraries
import urllib.request
import numpy as np
import sys
from bs4 import BeautifulSoup
from pathlib import Path

import requests

print("\033[0;37;41m#####      Covid-19-AI      #####")
print("")
print("")
print("By @stephane_branly")
print("https://github.com/StephaneBranly")

month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_start = '01-22-2020'
date_end = input("Write the end data date (mm-dd-yyyy) : ")

print()
print("# Downloading data from github")
print()

date_start = date_start.split('-')
date_end = date_end.split('-')

data_table = []
data_current_file = []
data_current_line = []

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
        if(soup != ""):
            data_current_file = str(soup)
            data_current_file = data_current_file.replace("\r", "")
            data_current_file = data_current_file.split("\n")
            for i in range(1, len(data_current_file)):
                data_current_line = data_current_file[i].split(',')
                if(data_current_line != [""]):
                    data_table.append(data_current_line)
    print("")


print("Result:")
