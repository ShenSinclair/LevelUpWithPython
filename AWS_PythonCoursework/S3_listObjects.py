#This python script lists objects located in an s3 bucket

import boto3

s3_resource=boto3.client("s3")
objects = s3_resource.list_objects(Bucket="sheniellspythonbucket")["Contents"]
print(objects)
print(len(objects))