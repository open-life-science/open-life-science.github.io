#!/usr/bin/env bash

python bin/prepare_website_data.py \
    createcalltemplate \
    --schedule_url "https://docs.google.com/spreadsheets/d/1Tnk-kkHUmPOEfUOEAl627l6JS9SoY5D4gSAPCYoBRSY/export?format=csv&gid=2109933309" \
    --output "ols-calls"
