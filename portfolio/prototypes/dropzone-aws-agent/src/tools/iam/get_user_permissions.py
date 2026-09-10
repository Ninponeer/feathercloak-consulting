from langchain_core.tools import tool
from src.clients.iam import get_iam_client

@tool
def get_user_permissions(user_name: str) -> dict:
    """Get the attached policies for an IAM user."""
    iam = get_iam_client()
    try:
        response = iam.list_attached_user_policies(UserName=user_name)
        policies = response.get("AttachedPolicies", [])
        return {"UserName": user_name, "Policies": policies}
    except Exception as e:
        return {"Error": str(e)}