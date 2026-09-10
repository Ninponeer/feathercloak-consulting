from langchain_core.tools import tool
from src.clients.s3 import get_s3_client

@tool
def get_s3_bucket_acl(bucket_name: str) -> dict:
    """Get the ACL for the given S3 bucket."""
    s3 = get_s3_client()
    try:
        response = s3.get_bucket_acl(Bucket=bucket_name)
        return {"acl": response}
    except Exception as e:
        return {"Error": f"Error getting S3 bucket ACL for bucket {bucket_name}: {e}"}