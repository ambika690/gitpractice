import boto3
client = boto3.client("ec2", region_name="us-east-1")
response = client.run_instances(
    ImageId='ami-071226ecf16aa7d96',
    InstanceType='t2.micro',
    KeyName= 'pythontest',
    MaxCount=1,
    MinCount=1
)
)
updated in git_hub
