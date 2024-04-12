#!/bin/bash

URL=${1:-https://packtheflag.dctf.si/}

curl "$URL" \
  -H 'Content-Type: application/json' \
  --data-raw '{"task_list":["Task 1","Task 2","Task 3","asd"],"user":"admin"}' -vv
