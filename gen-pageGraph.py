
# -*- coding: utf-8 -*-

from webweb import Web 
import os, csv                                                                                                                                                          

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

with open(space_key+'_pageEdges.csv','r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader, None)  # skip the input CSV headers [1][2]
    pageEdges = list(reader)

Web(pageEdges).save(space_key+'_pageGraph.html')