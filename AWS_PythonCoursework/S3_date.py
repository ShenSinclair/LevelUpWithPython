#Python script which prints s3 bucket name and creation date attributes

import boto3
s3_resource=boto3.client("s3")
s3_resource.list_buckets()

print(s3_resource)
print(s3_resource.list_buckets()["Buckets"])
print(s3_resource.list_buckets()["Buckets"][0]["Name"])
print(s3_resource.list_buckets()["Buckets"][0]["CreationDate"])

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])