import argparse
import logging
from pathlib import Path
from src.agents.stava_agent import StavaAgent

# filepath: c:\bitbucket\feathercloak\private-portfolio\dropzone.ai\agent_runner.py

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Stava Agent Runner - AWS Resource Inspector",
        epilog="""
        Examples:
        python agent_runner.py "How many S3 buckets are exposed to the public?"
        python agent_runner.py "What data does the S3 bucket my-bucket hold?"
        python agent_runner.py "What is the size of the EC2 instance with IP 10.0.1.5?"
        python agent_runner.py "What permissions does the user admin have?"
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "question",
        type=str,
        help="Question / query to pass to the Stava agent to inspect AWS resources"
    )


# Future enhancement - add support for different agent execution modes (single / strict / supervised)
#    parser.add_argument(
#        "--mode",
#        choices=["single", "strict", "supervised"],
#        default="single",
#        help="Execution mode for the agent"
#    )
#    parser.add_argument(
#    parser.add_argument(
#        "--input",
#        type=str,
#        required=True,
#        help="User query for the agent to process"
#    )
#    parser.add_argument(
#        "--max-calls",
#        type=int,
#        default=3,
#        help="Maximum tool calls for supervised/strict modes"
#    )

    args = parser.parse_args()

    logger.info("Initializing Stava Agent")
    agent = StavaAgent()

    logger.info(f"Processing query: {args.question}")
    result = agent.run(args.question)

    print("\n" + "=" * 80)
    print("STAVA AGENT OUTPUT")
    print("=" * 80)
    print(result)


if __name__ == "__main__":
    main()