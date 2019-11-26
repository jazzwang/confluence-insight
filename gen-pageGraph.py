# -*- coding: utf-8 -*-

import os, csv
import pandas as pd
from webweb import Web 

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

with open(space_key+'_pageLinks.csv','r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader, None)  # skip the input CSV headers [1][2]
    pageLinks = list(reader)

nodes = {}

df = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
for i in df[['contributor_id','contributor_name']].drop_duplicates().values.tolist():
    nodes[i[0]]={ 'name' :  i[1] , 'type' : 'contributor' }

for j in df['pageId'].drop_duplicates().values.tolist():
    nodes[j]={ 'type' : 'page' }

web = Web(
    adjacency=pageLinks,
    title=space_key,
    display={
        'nodes' : nodes
    },
)

#web.display.charge = 250
#web.display.linkLength = 50
web.display.height = 1024
web.display.width = 1280
web.display.colorBy = 'type'
web.display.sizeBy = 'degree'
#web.display.hideMenu = True
#web.display.showNodeNames = True

#web.show()
web.save(space_key+'_pageGraph.html')