# -*- coding: utf-8 -*-

import os, time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

try:
    home_url = os.environ["HOME_URL"]
    base_url = os.environ["BASE_URL"]
    space_key = os.environ["SPACE_KEY"]
except Exception as e:
    print("Please define environment variable 'BASE_URL' and 'SPACE_KEY'.")
    print("Ex: https://cwiki.apache.org/confluence/display/HADOOP")
    print("    HOME_URL  = https://cwiki.apache.org/confluence")
    print("    BASE_URL  = https://cwiki.apache.org")
    print("    SPACE_KEY = HADOOP")
    exit(1)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    if os.path.exists('storage_state.json'):
      print("[INFO] storage_state.json found. loading into browser context.")
      context = browser.new_context(storage_state='storage_state.json')
    else:
      context = browser.new_context()
    page = context.new_page()
    page.set_default_navigation_timeout(60000) # Set timeout to 60 seconds
    page.goto(home_url + "/pages/reorderpages.action?key=" + space_key)

    # Wait for the tree structure to load
    page.wait_for_selector(".closed")

    # Expand all closed tree nodes
    more_pages = True
    while more_pages:
        try:
            node = page.query_selector(".closed .click-zone")
            if node:
                node.click()
                time.sleep(0.1) # wait 100ms for UI to remove .closed status
            else:
                more_pages = False
        except Exception as e:
            more_pages = False
            break

    # Write CSV headers
    pages = open(space_key + '_pages.csv', 'w+')
    print("page_url", file=pages)

    soup = BeautifulSoup(page.content(), "lxml")

    for block in soup.select('#tree-div a[href^="/"]'):
        print(base_url + block.get('href'), file=pages)

    page.context.storage_state(path='storage_state.json')
    time.sleep(10) # wait 10 seconds before closing
    browser.close()