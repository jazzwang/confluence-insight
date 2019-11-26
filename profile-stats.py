#!env python
# -*- coding: utf-8 -*-

import os, sys, re, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " WIKI_URL")
    sys.exit(1)

driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get(sys.argv[1])

# Recursive condition to expand all closed tree
more_pages = True
while more_pages:
    try:
        driver.find_element_by_class_name("more-link").click()
        time.sleep(1)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    except:
        more_pages = False

soup = BeautifulSoup(driver.page_source,"lxml")
print(soup.prettify())

driver.quit()
