#This python script uploads files to current s3 buckets

import boto3

#how to upload single file:

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="requirements.txt",
    Bucket="sheniellspythonbucket",
    Key="requirements.txt")
    