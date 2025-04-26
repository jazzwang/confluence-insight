# -*- coding: utf-8 -*-

## References:
## [1] https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
## [2] https://docs.python.org/3/library/functions.html#next

import os, csv, re, time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

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

pageIds = open(space_key+"_pageIds.csv","w+",512)

## Write CSV headers
print("page_url;pageId_url;pageId;page_size;attachments_count", file=pageIds)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    if os.path.exists('storage_state.json'):
      print("[INFO] storage_state.json found. loading into browser context.")
      context = browser.new_context(storage_state='storage_state.json')
    else:
      context = browser.new_context()
    page = context.new_page()
    page.set_default_navigation_timeout(60000) # Set timeout to 60 seconds

    for url in urls:
        page_url = url[0]
        page.goto(page_url)
        # wait for page to load
        page.wait_for_selector("#action-menu-link")
        page.click("#action-menu-link")

        soup = BeautifulSoup(page.content(), "lxml")

        for block in soup.select('#view-page-info-link'):
            pageId_url = base_url + block.get('href')
            pageId = pageId_url.split('=')[1]
            page_size = str(len(page.content()))

        attachments_count = re.split('[\\(\\)]',soup.select('.action-view-attachments span')[0].contents[2])[1]

        print(page_url + ";" + pageId_url + ";" + pageId + ";" + page_size + ";" + attachments_count, file=pageIds)

    page.context.storage_state(path='storage_state.json')
    time.sleep(10) # wait 10 seconds before closing
    browser.close()