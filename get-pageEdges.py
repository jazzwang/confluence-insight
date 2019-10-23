# -*- coding: utf-8 -*-

import os, csv
import pandas as pd

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

df = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
df.groupby(['contributor_id','pageId']).size().to_csv(space_key+'_pageEdges.csv')