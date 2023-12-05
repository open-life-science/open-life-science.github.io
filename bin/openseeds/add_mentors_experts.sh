#!/usr/bin/env bash

python bin/prepare_website_data.py addmentorsexperts \
    -p "openseeds"  \
    -c 6 \
    -t "mentor" \
    -du "https://docs.google.com/spreadsheets/d/1qZNk78paO54VNB_xvytuzKLlpcZtXMc6PezN4JMMcr8/export?format=csv&gid=1375310074"

python bin/prepare_website_data.py addmentorsexperts \
    -p "openseeds"  \
    -c 6 \
    -t "expert" \
    -du "https://docs.google.com/spreadsheets/d/1qZNk78paO54VNB_xvytuzKLlpcZtXMc6PezN4JMMcr8/export?format=csv&gid=1635903403"

