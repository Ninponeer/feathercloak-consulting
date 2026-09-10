"""
Minimal pytest smoke tests for Dropzone AI mock AWS resources.

These tests exercise the Moto-mocked clients created by the project's
`tests/mock_data.py` harness and verify the basic resources used by the tools.
"""
from tests.mock_data import setup_all_mock_data
from src.clients.s3 import get_s3_client
from src.clients.ec2 import get_ec2_client
from src.clients.iam import get_iam_client


def setup_module(module):
    # Initialize all mock AWS resources once per test module.
    setup_all_mock_data()


def test_s3_buckets_and_objects():
    s3 = get_s3_client()
    buckets = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
    assert "public-karaoke-lyrics" in buckets
    contents = s3.list_objects_v2(Bucket="public-karaoke-lyrics").get("Contents", [])
    keys = [o["Key"] for o in contents]
    assert any("never_gonna_give_you_up" in k for k in keys)


def test_s3_bucket_acl_public():
    s3 = get_s3_client()
    acl = s3.get_bucket_acl(Bucket="public-karaoke-lyrics")
    grants = acl.get("Grants", [])
    uris = [
        g.get("Grantee", {}).get("URI")
        for g in grants
        if isinstance(g.get("Grantee", {}), dict)
    ]
    assert any(uri and "AllUsers" in uri for uri in uris)


def test_ec2_instances():
    ec2 = get_ec2_client()
    resp = ec2.describe_instances(Filters=[{"Name": "private-ip-address", "Values": ["10.0.1.5"]}])
    reservations = resp.get("Reservations", [])
    assert reservations, "No reservations for IP 10.0.1.5"
    instances = reservations[0].get("Instances", [])
    assert instances, "No instances in reservation"
    assert instances[0].get("InstanceType") in ("t2.micro", "t3.large")


def test_iam_user_policies():
    iam = get_iam_client()
    resp = iam.list_attached_user_policies(UserName="totally-legitimate-admin")
    policies = resp.get("AttachedPolicies", [])
    assert any(p.get("PolicyName") == "AdminPolicy" for p in policies)
