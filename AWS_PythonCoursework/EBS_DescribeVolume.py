import boto3

ec2_boto3=boto3.client("ec2")

x=ec2_boto3.describe_snapshots(SnapshotIds=['snap-03e31559b07b6eadd'
        ])
        
print(x)