import boto3

ec2_client=boto3.client("ec2")

x=ec2_client.create_volume(AvailabilityZone='us-east-1b',
        Encrypted=False,
        Size=12,
        SnapshotId='snap-09ec39a0ecf380fba',
        VolumeType='gp2')
        
print(x)