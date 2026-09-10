from langchain_core.tools import tool
from src.clients.s3 import get_s3_client


@tool
def get_s3_object_content(bucket_name: str, key: str) -> str:
    """Return the UTF-8 decoded content of the object at `bucket_name`/`key`.

    If an error occurs, a brief error message is returned instead of raising.
    """
    s3 = get_s3_client()
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        body = response["Body"].read()
        return body.decode("utf-8", errors="replace")
    except Exception as e:
        return f"Error retrieving S3 object {bucket_name}/{key}: {str(e)}"
