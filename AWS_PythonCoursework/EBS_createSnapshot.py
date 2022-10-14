import boto3

ec2_client=boto3.client("ec2")

x=ec2_client.create_snapshot( Description= 'snapshot from basevolume using python',
        VolumeId='vol-04fcf04c96dfd2549')
        
print(x)