#!/bin/bash
export HOME_URL=https://cwiki.apache.org/confluence
export BASE_URL=https://cwiki.apache.org
if [ "$1" == "" ]; then
    export SPACE_KEY=HADOOP
else
    export SPACE_KEY=$1
fi
python3 get-pages.py
python3 get-pageIds.py
python3 get-pageHistories.py
python3 get-pageLinks.py
python3 gen-pageGraph.py
