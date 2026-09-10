from langchain_core.tools import tool
from src.clients.ec2 import get_ec2_client

@tool
def describe_ec2_instance(private_ip: str) -> dict:
    """Describe an EC2 instance by its private IP address."""
    ec2 = get_ec2_client()
    try:
        response = ec2.describe_instances(
            Filters=[{"Name": "private-ip-address", "Values": [private_ip]}]
        )
        reservations = response.get("Reservations", [])
        if reservations:
            instances = reservations[0].get("Instances", [])
            if instances:
                inst = instances[0]
                return {
                    "InstanceId": inst.get("InstanceId"),
                    "InstanceType": inst.get("InstanceType"),
                    "PrivateIpAddress": inst.get("PrivateIpAddress"),
                    "State": inst.get("State", {}).get("Name"),
                }
        return {"error": f"No EC2 instance found for private ip {private_ip}"}
    except Exception as e:
        return {"error": f"Error describing EC2 instance {private_ip}: {e}"}