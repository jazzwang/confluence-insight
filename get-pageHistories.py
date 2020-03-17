# -*- coding: utf-8 -*-

## References:
## [1] https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
## [2] https://docs.python.org/3/library/functions.html#next

import os, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

driver = webdriver.Chrome()
## https://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(10) # seconds

## https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
## defaul buffer size = 8192 (8 KB)
## change to 512 Bytes
## make it flush to dish faster because I use `wc` to check the progress of each task
pageHistories = open(space_key+"_pageHistories.csv","w+", 512)
## Write CSV headers
print("pageId;version;published;contributor_id;contributor_name", file = pageHistories)

for pageId in pageIds:
    driver.get(home_url + "/pages/viewpreviousversions.action?pageId=" + pageId[2])
    soup = BeautifulSoup(driver.page_source,"lxml")
    cols = soup.select("#page-history-container tbody tr td")
    count = int(cols[0].find('input').get('value'))
    for i in range(count):
        try:
            version          = cols[6*i].find('input').get('value')
            published        = cols[6*i+2].contents[0].lstrip().rstrip()
            contributor_id   = cols[6*i+3].find('div').get('data-username')
            contributor_name = cols[6*i+3].find('a').contents[0]
        except AttributeError: 
            print("#Exception `AttributeError` ----------------------")
            print(cols[6*i+3])
            contributor_id   = "anonymous"
            contributor_name = "Anonymous"

        print(pageId[2] + ";" + version + ";" + published + ";" + contributor_id + ";" + contributor_name, file = pageHistories)

driver.quit()