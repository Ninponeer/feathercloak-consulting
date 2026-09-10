from langchain_core.tools import tool
from src.clients.s3 import get_s3_client

@tool
def list_s3_objects(bucket_name: str, prefix: str = "") -> list[str]:
    """List objects in an S3 bucket with an optional prefix."""
    s3_client = get_s3_client()
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except Exception as e:
        return [f"Error listing S3 objects: {str(e)}"]
