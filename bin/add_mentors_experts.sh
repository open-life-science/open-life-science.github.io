#!/usr/bin/env bash

[ ! -e "mentor_update" ] || rm "mentor_update"
python bin/prepare_website_data.py addmentorsexperts \
    -c 5 \
    -t "mentor" \
    -du "https://docs.google.com/spreadsheets/d/1cf_eT5_GSw3kH6W4BKpzYTeXCqwVzlaig16XyPpte0Q/export?format=csv&gid=1347834503"

[ ! -e "expert_update" ] || rm "expert_update"
python bin/prepare_website_data.py addmentorsexperts \
    -c 5 \
    -t "expert" \
    -du "https://docs.google.com/spreadsheets/d/1cf_eT5_GSw3kH6W4BKpzYTeXCqwVzlaig16XyPpte0Q/export?format=csv&gid=830320790"

