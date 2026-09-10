def extract_bucket_names(resp):
    return [b["Name"] for b in resp.get("Buckets", [])]