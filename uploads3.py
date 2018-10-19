#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
        import pip
        pip.main(["install","boto3"])
        import boto3
except Exception as e:
        print("boto3 not installed: "+str(e))
	sys.exit(1)

ACCESS_KEY_ID=""
SECRET_ACCESS_KEY=""
bucketname="S3 bucket name"   # example: "sqldumps"
localfile="Local file path to upload to s3 " # example: "/tmp/dump.sql"
key="S3 bucket path" # example: "2018_DUMPS/dump.sql"
 
s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=SECRET_ACCESS_KEY)
bucket = s3.Bucket(bucketname)
bucket.put_object(Body=open(localfile,'rb'), Key=key)

# Script will upload the file to this s3 path : sqldumps/2018_DUMPS/dump.sql
