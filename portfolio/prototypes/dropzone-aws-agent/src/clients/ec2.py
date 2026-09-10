import os
import boto3
from moto import mock_aws

# Initialize moto mock
mock = mock_aws()
mock.start()


def get_ec2_client():
    region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
    return boto3.client("ec2", region_name=region)