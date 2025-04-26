# -*- coding: utf-8 -*-

import os, csv, time
import pandas as pd
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

with open(space_key+'_pageIds.csv','r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader, None)  # skip the input CSV headers [1][2]
    pageIds = list(reader)

url2pageId = {}

for pageId in pageIds:
    url2pageId[pageId[0]] = pageId[2]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    if os.path.exists('storage_state.json'):
      print("[INFO] storage_state.json found. loading into browser context.")
      context = browser.new_context(storage_state='storage_state.json')
    else:
      context = browser.new_context()
    page = context.new_page()
    page.set_default_navigation_timeout(60000) # Set timeout to 60 seconds

    ## https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
    ## default buffer size = 8192 (8 KB)
    ## change to 512 Bytes
    ## make it flush to dish faster because I use `wc` to check the progress of each task
    pageLinks = open(space_key+"_pageLinks.csv","w+",512)
    ## Write CSV headers
    print("pageId;linkedId", file = pageLinks)

    for pageId in pageIds:
        page.goto(pageId[1])
        page.wait_for_selector("#action-menu-link")     # make sure that the page is loaded correctly
        soup = BeautifulSoup(page.content(), "lxml")
        cols = soup.select("table.pageInfoTable a[href^='/']")
        for i in cols:
            url = base_url + i.get('href')
            if url in url2pageId:
                print(pageId[2] + ";" + url2pageId[url], file = pageLinks)

    page.context.storage_state(path='storage_state.json')
    time.sleep(10) # wait 10 seconds before closing
    browser.close()

## add "pageId - contributor_id"
df = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
for i in df[['pageId','contributor_id']].drop_duplicates().values.tolist():
    print(str(i[0]) + ";" + i[1], file = pageLinks)

pageLinks.flush()
pageLinks.close()