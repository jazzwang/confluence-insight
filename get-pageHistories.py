# -*- coding: utf-8 -*-

## References:
## [1] https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
## [2] https://docs.python.org/3/library/functions.html#next

import os, csv
import pandas as pd  # Import pandas library
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
    pageHistories = open(space_key+"_pageHistories.csv","w+", 512)
    ## Write CSV headers
    print("pageId;version;published;contributor_id;contributor_name", file = pageHistories)

    for pageId in pageIds:
        page.goto(home_url + "/pages/viewpreviousversions.action?pageId=" + pageId[2])
        page.wait_for_selector("#action-menu-link")     # make sure that the page is loaded correctly
        soup = BeautifulSoup(page.content(), "lxml")
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

    pageHistories.close()

    df1 = pd.read_csv(space_key+"_pageIds.csv", sep=';')
    df2 = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
    df3 = pd.merge(df1,df2,on='pageId')
    df3.to_csv(space_key+"_pageMerged.csv")

page.context.storage_state(path='storage_state.json')
browser.close()
