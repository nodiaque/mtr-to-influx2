# mtr-to-influx2
Python script that redirect mtr output to an influx v2 database.

MTR will be ran using the ips/hostname in the list-ip-dest file for the number of cycle defined by the environment variable CYCLE and will wait between each full run for the number of seconds set in INTERVAL.

Prerequisite
This script rely on environment variable to be used in a docker situation.

INTERVAL=int - Number of seconds to wait between each full run
CYCLE=int - Number of MTR cycle to run against each host
BUCKET="your bucket name" - Name of the bucket to use in influxdb
ORG="your org name" - Name of the organization to use in influxdb
TOKEN="your api token" - The API Token generated in influxdb that have write access to bucket in org
URL="url to influxdb" - URL to the influxdb with port. Usually, something like http://ip:8086

Usage

./mtr-exporter.sh 
