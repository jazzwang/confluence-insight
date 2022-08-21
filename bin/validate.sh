#!/bin/bash
SPACE=$1
echo "History:"
sort ${SPACE}_pageHistories.csv | awk -F';' '{ print $1 }' | uniq | sort | wc
echo "Links:"
sort ${SPACE}_pageLinks.csv | awk -F';' '{ print $1 }' | uniq | sort | wc
echo "PageIDs:"
sort ${SPACE}_pageIds.csv | awk -F';' '{ print $1 }' | uniq | sort | wc
echo "Pages:"
sort ${SPACE}_pages.csv | awk -F';' '{ print $1 }' | uniq | sort | wc
echo "-----"
wc ${SPACE}_page*.csv
