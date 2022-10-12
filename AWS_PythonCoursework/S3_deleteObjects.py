# This script deletes ojects from s3 buckets.

import boto3

s3_resource=boto3.client("s3")

s3_resource.delete_object(Bucket='sheniellspythonbucket',
    Key="requirements.txt")