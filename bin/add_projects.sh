#!/usr/bin/env bash

python bin/prepare_website_data.py \
    addprojects \
    -c 7 \
    -pu "https://docs.google.com/spreadsheets/d/1DQ3Ugsu25UL4EgoD5KYQHWe1R5OW6Er1fl9r71GPHYw/export?format=csv&gid=1211583826" \
    -du "https://docs.google.com/spreadsheets/d/1hVPr5E79JdBRkF52viZiFuefnh2DLVkq/export?format=csv&gid=1335178488"