import boto3

ec2_client=boto3.client('ec2')

x=ec2_client.delete_snapshot(SnapshotId='snap-03b8470f2a4a34a6d')

print(x)