#!/bin/bash

function monitor_mtr() {
  for MTR_HOST in $(cat ./list-ip-dest); do
    ( mtr --report --tcp --port=443 --json --report-cycles $CYCLE $MTR_HOST | /usr/bin/python3 ./save_data.py ) &
  done
}

which mtr &>/dev/null
if [ $? -eq 1 ]; then
  echo "mtr not found, please install mtr "
  exit 1
fi 

if [ -z "$INTERVAL" ]; then
  echo "INTERVAL not set"
  exit 1
fi

if [ -z "$CYCLE" ]; then
  echo "CYCLE not set"
  exit 1
fi

if [ -z "$BUCKET" ]; then
  echo "BUCKET not set"
  exit 1
fi

if [ -z "$ORG" ]; then
  echo "ORG not set"
  exit 1
fi

if [ -z "$TOKEN" ]; then
  echo "TOKEN not set"
  exit 1
fi

if [ -z "$URL" ]; then
  echo "URL not set"
  exit 1
fi

echo "collectin data..."
while true; do
  monitor_mtr
  sleep $INTERVAL
done
