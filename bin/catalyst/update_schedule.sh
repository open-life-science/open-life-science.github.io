#!/usr/bin/env bash

 echo "CAT-1"
 python bin/prepare_website_data.py \
     updateschedule \
     --program 'catalyst' \
     --cohort '1' \
     --schedule_url "https://docs.google.com/spreadsheets/d/1oJxz-SXcqC4AnvLAGRPjiw5JyCEZNTskteLf6n-yZ7o/export?format=csv&gid=2109933309"