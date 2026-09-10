"""Small CLI to fetch random Chuck Norris facts from the mock S3 bucket.

This bypasses the LLM path and directly calls the helper in the tool
module so you can script and capture output reliably.
"""
import argparse
from tests.mock_data import setup_all_mock_data
from src.tools.s3.get_random_facts import get_random_facts


def main():
    parser = argparse.ArgumentParser(description="Fetch random facts from S3 bucket")
    parser.add_argument("--bucket", "-b", default="chuck-norris-facts", help="S3 bucket name")
    parser.add_argument("--count", "-n", type=int, default=5, help="Number of facts to return")
    args = parser.parse_args()

    # Ensure mock environment is initialized (creates buckets/objects)
    setup_all_mock_data()

    facts = get_random_facts.invoke({"bucket_name": args.bucket, "count": args.count})
    if isinstance(facts, list):
        for f in facts:
            print(f)
    else:
        print(facts)


if __name__ == "__main__":
    main()
