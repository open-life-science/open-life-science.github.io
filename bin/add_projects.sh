#!/usr/bin/env bash

python bin/prepare_website_data.py \
    addprojects \
    -c 6 \
    -pu "https://docs.google.com/spreadsheets/d/1m6qu2VSlA0HjjtWi91OrjG0f97NFmWS2eZcbmT2qMjs/export?format=csv&gid=1594045556" \
    -du "https://docs.google.com/spreadsheets/d/1Wyt_VvJBD5Dt5Vbt92Ta7vP15Y4qBV1bAOxLQwPT1JM/export?format=csv&gid=2071926975"