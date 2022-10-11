#This script allows you to search and print the number of S3 buckets that are available 
import boto3

resource=boto3.resource 
resource=boto3.resource("s3")
list(resource.buckets.all())

print(list(resource.buckets.all()))

print(len(list(resource.buckets.all())))