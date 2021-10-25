#!/usr/bin/env bash

[ ! -e "mentor_update" ] || rm "mentor_update"
python bin/extractpeople.py \
    --url "https://docs.google.com/spreadsheets/d/1n-cZTJI27kfrXmvIWYIFQXab_27EArm2C-QBnkSY7iM/export?format=csv&gid=1983788876" \
    >> "mentor_update"

[ ! -e "expert_update" ] || rm "expert_update"
python bin/extractpeople.py \
    --url "https://docs.google.com/spreadsheets/d/1n-cZTJI27kfrXmvIWYIFQXab_27EArm2C-QBnkSY7iM/export?format=csv&gid=75468187" \
    >> "expert_update"