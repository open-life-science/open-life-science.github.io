#!/usr/bin/env bash

python bin/prepare_website_data.py addmentorsexperts \
    -c 5 \
    -t "mentor" \
    -du "https://docs.google.com/spreadsheets/d/1cf_eT5_GSw3kH6W4BKpzYTeXCqwVzlaig16XyPpte0Q/export?format=csv&gid=1347834503"

python bin/prepare_website_data.py addmentorsexperts \
    -c 5 \
    -t "expert" \
    -du "https://docs.google.com/spreadsheets/d/1cf_eT5_GSw3kH6W4BKpzYTeXCqwVzlaig16XyPpte0Q/export?format=csv&gid=830320790"

