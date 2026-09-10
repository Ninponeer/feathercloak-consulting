from langchain_core.tools import tool
from src.clients.s3 import get_s3_client
import json
import random
from typing import List


@tool
def get_random_facts(bucket_name: str, count: int = 5) -> List[str]:
    """Return up to `count` random facts from the given S3 bucket.

    Prefers `facts.json` at the bucket root, falls back to objects with prefix `fact_`.
    """
    s3 = get_s3_client()
    facts: List[str] = []

    # Try structured file first
    try:
        obj = s3.get_object(Bucket=bucket_name, Key="facts.json")
        facts = json.loads(obj["Body"].read().decode("utf-8"))
        if not isinstance(facts, list):
            facts = [str(facts)]
    except Exception:
        # Fallback to individual fact_*.txt objects
        try:
            resp = s3.list_objects_v2(Bucket=bucket_name, Prefix="fact_")
            keys = [o["Key"] for o in resp.get("Contents", [])] if resp.get("Contents") else []
            for k in keys:
                try:
                    o = s3.get_object(Bucket=bucket_name, Key=k)
                    facts.append(o["Body"].read().decode("utf-8", errors="replace"))
                except Exception:
                    continue
        except Exception as e:
            return [f"No facts found in bucket {bucket_name}: {str(e)}"]

    if not facts:
        return [f"No facts found in bucket {bucket_name}"]

    n = min(int(count), len(facts))
    return random.sample(facts, k=n)
