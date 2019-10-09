# -*- coding: utf-8 -*-

# References: 
# [1] https://kite.com/python/examples/4420/beautifulsoup-parse-an-html-table-and-write-to-a-csv

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
    pageIds = list(reader)

driver = webdriver.Chrome()
pageHistories = open(space_key+"_pageHistories.csv","w+")

for pageId in pageIds:
    driver.get(home_url + "/pages/viewpreviousversions.action?pageId=" + pageId[2])
    soup = BeautifulSoup(driver.page_source,"lxml")
    table = soup.find(id = "page-history-container")
    cols = table.select('td')
    version = cols[0].find('input').get('value')
    published = cols[2].contents[0].lstrip().rstrip()
    contributor_id = cols[3].find('img').get('title')
    contributor_name = cols[3].find('a').contents[0]
    print(version + ";" + published + ";" + contributor_id + ";" + contributor_name)