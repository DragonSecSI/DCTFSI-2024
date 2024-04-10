#!/bin/bash

[ -z "$1" ] && echo "Usage: $0 <base_url>" && exit 1

url=$1
curl "$url" \
  -H 'Content-Type: application/json' \
  --data-raw '{"task_list":["Task 1","Task 2","Task 3","asd"],"user":"admin"}' -vv
