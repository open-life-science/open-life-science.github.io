#!/usr/bin/env bash#
ACTIVE_COHORT=6
NEXT_COHORT=$((ACTIVE_COHORT+1))
EXPORT_URL="https://docs.google.com/spreadsheets/d/1jXJH8J4MKee80ODcgWoxpvPkV8ob0tw86Fov8nlXxXw/export?format=csv&gid=1181436982"
#python bin/prepare_website_data.py \
#    updateschedule \
#    --cohort '4' \
#    --schedule_url "https://docs.google.com/spreadsheets/d/1-mNA_IcGYkr2b92QpGyD9qSeN5OC5T5d1p5hhM_fVYw/export?format=csv&gid=1181436982"

#python bin/prepare_website_data.py \
#    updateschedule \
#    --cohort '5' \
#    --schedule_url "https://docs.google.com/spreadsheets/d/1qkbOOzS-60WmSUVmWLwd7zpRBQI0fkaMeFrCXN_pyUk/export?format=csv&gid=1181436982"

python bin/prepare_website_data.py \
    updateschedule \
    --cohort "$NEXT_COHORT" \
    --schedule_url "$EXPORT_URL"

#python bin/prepare_website_data.py \
#    updateschedule \
#    --cohort '7' \
#    --schedule_url "https://docs.google.com/spreadsheets/d/1jXJH8J4MKee80ODcgWoxpvPkV8ob0tw86Fov8nlXxXw/export?format=csv&gid=1181436982"

#python bin/prepare_website_data.py \
#    updateschedule \
#    --cohort '8' \
#    --schedule_url "https://docs.google.com/spreadsheets/d/1Tnk-kkHUmPOEfUOEAl627l6JS9SoY5D4gSAPCYoBRSY/export?format=csv&gid=1181436982"
