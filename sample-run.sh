#!/bin/bash
export HOME_URL=https://cwiki.apache.org/confluence
export BASE_URL=https://cwiki.apache.org
export SPACE_KEY=HADOOP
python3 get-pages.py
python3 get-pageIds.py
python3 get-pageHistories.py
