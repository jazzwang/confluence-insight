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
    print("Ex: HOME_URL  = https://cwiki.apache.org/confluence/display/HADOOP2")
    print("    BASE_URL  = https://cwiki.apache.org")
    print("    SPACE_KEY = HADOOP2")
    exit(1)

with open(space_key+'_links.csv','r') as f:
    reader = csv.reader(f)
    urls = list(reader)

driver = webdriver.Chrome()
pageIds = open(space_key+"_pageIds.csv","w+")

for url in urls:
        source_url = url[0]
        driver.get(source_url)
        driver.find_element_by_id("action-menu-link").click()
        soup = BeautifulSoup(driver.page_source,"lxml")
        
        for block in soup.select('#view-page-info-link'):
            target_url = base_url + block.get('href')
            pageId = target_url.split('=')[1]
            print(source_url + ";" + target_url + ";" + pageId, file=pageIds)
        
driver.quit()