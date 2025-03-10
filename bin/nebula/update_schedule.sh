#!/usr/bin/env bash

echo "NEB-1"
python bin/prepare_website_data.py \
    updateschedule \
    -p "nebula"  \
    --cohort '1' \
    --schedule_url "https://docs.google.com/spreadsheets/d/15cR5YsttvmbtX8q_Zt4YBangzqns3NqkisJFf3_ApZI/export?format=csv&gid=1514825681"