"""
🎭 Mock AWS Data Setup — The Forge's Test Harness

> *"Never gonna give you up, never gonna let you down..."*  
> — Rick Astley (and also this test suite's philosophy)

## 📜 What This Does

Creates a beautiful disaster of mock AWS resources for testing the Stava agent.
Because testing against production is for people who enjoy living dangerously.

## 🎯 Mock Resources Created

- **S3 Buckets**: A mix of public embarrassments and private secrets
- **EC2 Instances**: Definitely not mining cryptocurrency
- **IAM Users**: With permissions ranging from "god mode" to "can barely read"

## 🚧 Status

✅ Fully functional chaos  
✅ Rick Astley approved  
✅ No actual AWS resources harmed in the making of this test suite

---

*"Slow is Smooth, Smooth is Fast" — except when mocking AWS, then it's just fast.*
"""
import json
from src.clients.s3 import get_s3_client
from src.clients.ec2 import get_ec2_client
from src.clients.iam import get_iam_client


def setup_mock_s3_data():
    """
    Create mock S3 buckets with various ACL configurations.
    
    Some are public (because security is just a suggestion, right?).
    Some are private (because we learned from our mistakes... maybe).
    """
    s3 = get_s3_client()
    
    # Create buckets with increasingly questionable names
    buckets = [
        "definitely-not-secrets",           # Narrator: It was secrets
        "nothing-to-see-here",              # Move along, citizen
        "public-karaoke-lyrics",            # Rick Astley's greatest hits
        "secure-backup-no-really"           # We promise this time
    ]
    
    for bucket_name in buckets:
        s3.create_bucket(Bucket=bucket_name)
    
    # Add some objects with... personality
    s3.put_object(
        Bucket="definitely-not-secrets",
        Key="passwords.txt",
        Body=b"admin:password123\nroot:hunter2\n# TODO: Change these before production"
    )
    
    s3.put_object(
        Bucket="public-karaoke-lyrics",
        Key="never_gonna_give_you_up.txt",
        Body=b"""We're no strangers to love
                You know the rules and so do I
                A full commitment's what I'm thinking of
                You wouldn't get this from any other guy

                I just wanna tell you how I'm feeling
                Gotta make you understand

                Never gonna give you up
                Never gonna let you down
                Never gonna run around and desert you
                Never gonna make you cry
                Never gonna say goodbye
                Never gonna tell a lie and hurt you

                -- Rick Astley (1987)

                P.S. If you're reading this in a security audit, congratulations on being Rick-rolled.
                """
    )
    
    s3.put_object(
        Bucket="nothing-to-see-here",
        Key="README.md",
        Body=b"# Nothing To See Here\n\nSeriously. Just a normal bucket. Definitely not hiding anything.\n\n*nervous whistling*"
    )
    
    s3.put_object(
        Bucket="secure-backup-no-really",
        Key="backup_2026_04_15.tar.gz",
        Body=b"Definitely real backup data and not just random bytes"
    )
    
    # Make some buckets public (because YOLO)
    s3.put_bucket_acl(
        Bucket="public-karaoke-lyrics",
        ACL="public-read"  # Rick Astley's lyrics belong to the world
    )
    
    s3.put_bucket_acl(
        Bucket="nothing-to-see-here",
        ACL="public-read"  # Irony is our security model
    )

    # --- Chuck Norris Facts Bucket ---
    # Provide a small corpus of Chuck Norris "facts" as individual objects
    # and as a single JSON file so tests can exercise object listing and
    # content inspection.
    chuck_bucket = "chuck-norris-facts"
    s3.create_bucket(Bucket=chuck_bucket)

    chuck_facts = [
        "Chuck Norris can slam a revolving door.",
        "When Chuck Norris enters a room, he doesn't turn the lights on; he turns the dark off.",
        "Chuck Norris counted to infinity. Twice.",
        "The Boogeyman checks his closet for Chuck Norris.",
        "Chuck Norris can hear sign language.",
        "Chuck Norris doesn't flush the toilet; he scares the water into leaving.",
        "Chuck Norris can speak braille.",
        "Chuck Norris once won a game of Connect Four in three moves.",
        "Chuck Norris' keyboard doesn't have a Ctrl key because nothing controls Chuck Norris.",
        "Fear of heights is for people who can't reach Chuck Norris."
    ]

    for idx, fact in enumerate(chuck_facts, start=1):
        key = f"fact_{idx:03d}.txt"
        s3.put_object(Bucket=chuck_bucket, Key=key, Body=fact.encode("utf-8"))

    # Also add a JSON file with all facts for tests that prefer structured data
    s3.put_object(Bucket=chuck_bucket, Key="facts.json", Body=json.dumps(chuck_facts).encode("utf-8"))

    # Make the Chuck Norris facts publicly readable for any "public bucket" tests
    s3.put_bucket_acl(Bucket=chuck_bucket, ACL="public-read")


def setup_mock_ec2_data():
    """
    Create mock EC2 instances.
    
    Definitely not mining cryptocurrency. Definitely not running Skynet.
    Just normal, boring compute instances. Nothing to see here.
    """
    ec2 = get_ec2_client()
    
    # Create VPC and subnet first (because AWS makes us jump through hoops)
    vpc_response = ec2.create_vpc(CidrBlock="10.0.0.0/16")
    vpc_id = vpc_response["Vpc"]["VpcId"]
    
    subnet_response = ec2.create_subnet(VpcId=vpc_id, CidrBlock="10.0.1.0/24")
    subnet_id = subnet_response["Subnet"]["SubnetId"]
    
    # Launch instances with totally normal names
    ec2.run_instances(
        ImageId="ami-12345678",  # Definitely a real AMI
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",  # The "I'm on a budget" special
        SubnetId=subnet_id,
        PrivateIpAddress="10.0.1.5"
    )
    
    ec2.run_instances(
        ImageId="ami-8675309",  # Also definitely real
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.large",  # This one's for "development"
        SubnetId=subnet_id,
        PrivateIpAddress="10.0.1.10"
    )


def setup_mock_iam_data():
    """
    Create mock IAM users with policies.
    
    Permissions ranging from "I am become Death, destroyer of worlds"
    to "I can barely read my own email."
    """
    iam = get_iam_client()
    
    # Create users with varying levels of responsibility
    iam.create_user(UserName="totally-legitimate-admin")  # Seems legit
    iam.create_user(UserName="intern-with-prod-access")   # What could go wrong?
    iam.create_user(UserName="readonly-rick")             # Rick Astley fan account
    
    # Create custom policies (moto doesn't have AWS managed policies)
    admin_policy = iam.create_policy(
        PolicyName="AdminPolicy",
        PolicyDocument="""{
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]
        }"""
    )
    
    power_policy = iam.create_policy(
        PolicyName="PowerUserPolicy",
        PolicyDocument="""{
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Action": ["ec2:*", "s3:*"], "Resource": "*"}]
        }"""
    )
    
    readonly_policy = iam.create_policy(
        PolicyName="ReadOnlyPolicy",
        PolicyDocument="""{
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Action": ["ec2:Describe*", "s3:Get*", "s3:List*"], "Resource": "*"}]
        }"""
    )
    
    # Attach policies
    iam.attach_user_policy(
        UserName="totally-legitimate-admin",
        PolicyArn=admin_policy["Policy"]["Arn"]
    )
    
    iam.attach_user_policy(
        UserName="intern-with-prod-access",
        PolicyArn=power_policy["Policy"]["Arn"]
    )
    
    iam.attach_user_policy(
        UserName="readonly-rick",
        PolicyArn=readonly_policy["Policy"]["Arn"]
    )


def setup_all_mock_data():
    """
    Initialize all mock AWS resources.
    
    🎵 *Never gonna give you up, never gonna let you down...* 🎵
    
    This function is your one-stop shop for creating a complete mock AWS
    environment that's just chaotic enough to be interesting, but structured
    enough to actually test against.
    
    ## What Gets Created:
    - 4 S3 buckets (2 public, 2 private, all with personality)
    - 2 EC2 instances (definitely not mining crypto)
    - 3 IAM users (with permissions from god-mode to read-only)
    
    ## Why This Exists:
    Because testing against production is for people who enjoy living dangerously,
    and we prefer our chaos to be controlled and reproducible.
    
    — The Forge, April 2026
    """
    setup_mock_s3_data()
    setup_mock_ec2_data()
    setup_mock_iam_data()


if __name__ == "__main__":
    setup_all_mock_data()
    print("✅ Mock AWS data initialized successfully")
    print("🎵 You've been Rick-rolled by the test suite")
    print("🔥 The Forge burns bright, the mocks are ready")
