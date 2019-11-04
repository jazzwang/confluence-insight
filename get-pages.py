# -*- coding: utf-8 -*-
import os
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

driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get(home_url + "/pages/reorderpages.action?key=" + space_key)

# MEMO: exception handling - page take time to load
## https://selenium-python.readthedocs.io/waits.html
## https://selenium-python.readthedocs.io/api.html#locate-elements-by

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "closed"))
    )

# TODO: need to rewrite the recursive condition to expand all closed tree
more_pages = True
while more_pages:
    try:
        node = driver.find_element_by_class_name("closed")
        node.find_element_by_class_name("click-zone").click()
    except:
        more_pages = False

pages = open(space_key + '_pages.csv','w+')
## Write CSV headers
print("page_url",file=pages)

soup = BeautifulSoup(driver.page_source,"lxml")

for block in soup.select('#tree-div a[href^="/"]'):
    print(base_url + block.get('href'),file=pages)

#driver.quit()