# -*- coding: utf-8 -*-

## References:
## [1] https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
## [2] https://docs.python.org/3/library/functions.html#next

import os, csv, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

with open(space_key+'_pages.csv','r') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the input CSV headers [1][2]
    urls = list(reader)

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
## https://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(10) # seconds
## https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
## defaul buffer size = 8192 (8 KB)
## change to 512 Bytes
## make it flush to dish faster because I use `wc` to check the progress of each task
pageIds = open(space_key+"_pageIds.csv","w+",512)

## Write CSV headers
print("page_url;pageId_url;pageId;page_size;attachments_count", file=pageIds)

for url in urls:
        page_url = url[0]
        driver.get(page_url)
        driver.find_element_by_id("action-menu-link").click()
        soup = BeautifulSoup(driver.page_source,"lxml")
        
        for block in soup.select('#view-page-info-link'):
            pageId_url = base_url + block.get('href')
            pageId = pageId_url.split('=')[1]
            page_size = str(len(driver.page_source))

        attachments_count = re.split('[\(\)]',soup.select('.action-view-attachments span')[0].contents[2])[1]

        print(page_url + ";" + pageId_url + ";" + pageId + ";" + page_size + ";" + attachments_count, file=pageIds)

driver.quit()
