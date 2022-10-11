import boto3
resource=boto3.resource 
resource=boto3.resource("s3")
list(resource.buckets.all())

print(list(resource.buckets.all()))