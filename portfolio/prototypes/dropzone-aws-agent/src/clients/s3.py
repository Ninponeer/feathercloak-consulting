import os
import boto3
from moto import mock_aws

# Initialize moto mock
mock = mock_aws()
mock.start()


def get_s3_client():
    region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
    return boto3.client("s3", region_name=region)