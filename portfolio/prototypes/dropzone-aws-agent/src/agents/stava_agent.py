## Usage
#. python stava_agent.py --mode strict
#. python stava_agent.py --mode supervised
#. python stava_agent.py --single

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from src.tools.s3.list_buckets import list_s3_buckets
from src.tools.s3.get_bucket_acl import get_s3_bucket_acl
from src.tools.s3.list_objects import list_s3_objects
from src.tools.s3.get_object_content import get_s3_object_content
from src.tools.s3.get_random_facts import get_random_facts
from src.tools.ec2.describe_instance import describe_ec2_instance
from src.tools.iam.get_user_permissions import get_user_permissions
from tests.mock_data import setup_all_mock_data

import argparse
import json
import os
from pathlib import Path

# Load config
config_path = Path(__file__).parent.parent.parent / "config.json"
with open(config_path) as f:
    config = json.load(f)

# Set AWS credentials from config
os.environ["AWS_ACCESS_KEY_ID"] = config["aws"]["access_key_id"]
os.environ["AWS_SECRET_ACCESS_KEY"] = config["aws"]["secret_access_key"]
os.environ["AWS_DEFAULT_REGION"] = config["aws"]["region"]

model = config["ollama"]["model"]



class StavaAgent:
    def __init__(self, llm=None, tools=None):
        # Initialize mock AWS data
        setup_all_mock_data()
        
        # build the tool-calling agent
        self.llm = llm if llm is not None else ChatOllama(model=model)

        # build the agent tools list (ie. utility belt)
        self.tools = tools if tools is not None else [
            list_s3_buckets,
            get_s3_bucket_acl,
            list_s3_objects,
            get_random_facts,
            get_s3_object_content,
            describe_ec2_instance,
            get_user_permissions
        ]

        # Create the agent graph
        self.agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt="You are Stava, a tool-calling agent that can reason over AWS resources and call out to the tools at your disposal to inspect / enumerate S3 buckets, EC2 instances, and IAM user permissions."
        )
    
    def run(self, user_input: str) -> str:
        inputs = {"messages": [HumanMessage(content=user_input)]}
        result = self.agent.invoke(inputs)
        # Extract the final message content from the result
        messages = result.get("messages", [])
        if messages:
            return messages[-1].content
        return "No response generated"

    # NOT IMPLEMENTED - additional public methods for running the agent in different modes
    # \\\ - public methods - ///
    def run_single(self, user_input: str) -> str:
        # one-shot tool call
        pass

    def run_multi(self, user_input: str, mode="strict", max_calls: int = 3) -> str:
        # dispatch to strict or supervised
        pass

    # \\\ - private helpers - ///
    def _run_strict(self, user_input: str) -> str:
        pass

    def _run_supervised(self, user_input: str, max_calls: int) -> str:
        pass



