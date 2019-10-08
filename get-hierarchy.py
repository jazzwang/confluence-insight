# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import os

try:
    home_url  = os.environ["HOME_URL"]
    base_url  = os.environ["BASE_URL"]
    space_key = os.environ["SPACE_KEY"]
except:
    print("Please define environment variable 'BASE_URL' and 'SPACE_KEY'.")
    print("Ex: https://cwiki.apache.org/confluence/display/HADOOP2")
    print("    HOME_URL  = https://cwiki.apache.org/confluence")
    print("    BASE_URL  = https://cwiki.apache.org")
    print("    SPACE_KEY = HADOOP2")
    exit(1)

driver = webdriver.Chrome()
driver.get(home_url + "/pages/reorderpages.action?key=" + space_key)

# TODO: need to rewrite the recursive condition to expand all closed tree
more_pages = True
while more_pages:
    try:
        node = driver.find_element_by_class_name("closed")
        node.find_element_by_class_name("click-zone").click()
    except:
        more_pages = False

pages = open(space_key + '_links.csv','w+')

soup = BeautifulSoup(driver.page_source,"lxml")

for block in soup.select('#tree-div a[href^="/"]'):
    print(base_url + block.get('href'),file=pages)

driver.quit()