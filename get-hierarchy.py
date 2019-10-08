# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import os

try:
    base_url  = os.environ["BASE_URL"]
    space_key = os.environ["SPACE_KEY"]
except:
    print("Please define environment variable 'BASE_URL' and 'SPACE_KEY'.")
    print("If the confluence URL is 'https://cwiki.apache.org/confluence/display/HADOOP2',")
    print("BASE_URL  = https://cwiki.apache.org/confluence")
    print("SPACE_KEY = HADOOP2")
    exit(1)

driver = webdriver.Chrome()
driver.get(base_url + "/pages/reorderpages.action?key=" + space_key)

for x in range(5):
    try:
        node = driver.find_element_by_class_name("closed")
        node.find_element_by_class_name("click-zone").click()
    except:
        pass

pages = open(space_key + '_links.csv','w+')

soup = BeautifulSoup(driver.page_source,"lxml")

for block in soup.select('#tree-div a[href^="/"]'):
    print(block.get('href'),file=pages)

driver.quit()