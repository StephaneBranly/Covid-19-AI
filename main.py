# import libraries
import urllib.request
import numpy as np
import sys
from bs4 import BeautifulSoup

import requests

print("Welcome")
for i in range(1, 2):

    # specify the url
    quote_page = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-{:02d}-2020.csv".format(i)
    print(quote_page)
    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(quote_page)

    print(page)
