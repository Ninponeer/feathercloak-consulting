from langchain_core.tools import tool
from src.clients.s3 import get_s3_client

@tool
def list_s3_buckets() -> list[str]:
    """List all S3 bucket names in the AWS account."""
    s3 = get_s3_client()
    try:
        response = s3.list_buckets()
        return [bucket['Name'] for bucket in response.get('Buckets', [])]
    except Exception as e:
        return [f"Error listing S3 buckets: {e}"]