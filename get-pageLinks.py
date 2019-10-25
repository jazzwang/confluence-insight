# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import os, csv

try:
    home_url  = os.environ["HOME_URL"]
    base_url  = os.environ["BASE_URL"]
    space_key = os.environ["SPACE_KEY"]
except:
    print("Please define environment variable 'BASE_URL' and 'SPACE_KEY'.")
    print("Ex: https://cwiki.apache.org/confluence/display/HADOOP")
    print("    HOME_URL  = https://cwiki.apache.org/confluence")
    print("    BASE_URL  = https://cwiki.apache.org")
    print("    SPACE_KEY = HADOOP")
    exit(1)

with open(space_key+'_pageIds.csv','r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader, None)  # skip the input CSV headers [1][2]
    pageIds = list(reader)

url2pageId = {}

for pageId in pageIds:
    url2pageId[pageId[0]] = pageId[2]

driver = webdriver.Chrome()
pageLinks = open(space_key+"_pageLinks.csv","w+")
## Write CSV headers
print("pageId;linkedPageId", file = pageLinks)

for pageId in pageIds:
    driver.get(pageId[1])
    soup = BeautifulSoup(driver.page_source,"lxml")
    cols = soup.select("table.pageInfoTable a[href^='/']")
    for i in cols:
        url = base_url + i.get('href')
        if url in url2pageId:
            print(pageId[2] + ";" + url2pageId[url], file = pageLinks)

driver.quit()