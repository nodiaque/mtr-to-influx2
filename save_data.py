#!/usr/bin/env python3
import json
import sys
import datetime as dt
import logging
import os

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


logging.basicConfig(level=logging.INFO)


bucket = os.environ['BUCKET']
org = os.environ['ORG']
token = os.environ['TOKEN']
url=os.environ['URL']


def main():
    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )
    write_api = client.write_api(write_options=SYNCHRONOUS)


    mtr_result = json.load(sys.stdin)
    # ping destination
    destination = mtr_result['report']['mtr']['dst']
    report_time = dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    for hub in mtr_result['report']['hubs']:
        # persist the hub entry
        # Modifying the data if needed so that is can be easily sorted in the event of more than 9 hops.
        if len(str(hub['count'])) < 2:
            hop = "0" + str(hub['count']) + "-" + hub['host']
        else:
            hop = str(hub['count']) + "-" + hub['host']
         
        p = influxdb_client.Point("mtr").tag("destination",destination).tag("hop",hop).field("loss",hub['Loss%']).field("snt",hub['Snt']).field("last",hub['Last']).field("avg", hub['Avg']).field("best",hub['Best']).field("wrst",hub['Wrst']).field("stdev",hub['StDev']).field("time",report_time)
        
        write_api.write(bucket=bucket, org=org, record=p)


if __name__ == '__main__':
    main()
