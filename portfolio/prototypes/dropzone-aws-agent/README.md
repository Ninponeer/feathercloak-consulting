# Dropzone AI – AWS Chatbot (Take-Home)
Author: Rick Metz

Minimal, functional example of a LangChain agent augmented with AWS tools.
Includes moto-based mocks and a small test harness so the project can be
run locally without real AWS credentials.

Requirements
- Python 3.10–3.12
- pip
- (Optional) Ollama runtime if you want to exercise the LLM path

Quick start (Windows PowerShell)
```powershell
cd portfolio\prototypes\dropzone-aws-agent
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Run tests (verifies tools against moto mocks)
```powershell
python -m pytest -q
# Expected: smoke tests pass (examples: S3/EC2/IAM smoke tests)
```

Quick verification (no Ollama required)
- Fetch 5 random Chuck Norris facts (reads moto-mocked S3 data):
```powershell
python get_chuck_facts.py --count 5 > outputs\q_bucket_just_the_facts.txt
Get-Content outputs\q_bucket_just_the_facts.txt -Raw
```

Run the agent (LLM path — requires Ollama)
1. Start your Ollama runtime and ensure the model in `config.json` is available.
2. Run:
```powershell
python agent_runner.py "How many S3 buckets are exposed to the public?"
```

Files of interest
- [agent_runner.py](agent_runner.py) — CLI wrapper around `StavaAgent`
- [get_chuck_facts.py](get_chuck_facts.py) — direct CLI to validate S3 tooling
- [src/agents/stava_agent.py](src/agents/stava_agent.py) — agent wiring + tools
- [src/tools](src/tools) — LangChain tools for S3, EC2, IAM (see `s3/`, `ec2/`, `iam/`)
- [tests/mock_data.py](tests/mock_data.py) and [tests/test_smoke.py](tests/test_smoke.py) — moto mocks and smoke tests
- `outputs/` — example output files produced during development

Tool-to-question mapping
- Count public S3 buckets: `list_s3_buckets` + `get_s3_bucket_acl`
- Inspect bucket contents: `list_s3_objects` then `get_s3_object_content`
- EC2 instance size by IP: `describe_ec2_instance` (returns `InstanceType`)
- IAM user permissions: `get_user_permissions` (attached policies)
- Extra helper: `get_random_facts` (returns random facts from `facts.json` or `fact_*.txt`)

Security
- `config.json` contains non-production test values. Do not commit real keys.
- Tests use `moto` and do not call real AWS services.

If you need a deterministic demo without Ollama, run the tests and/or `get_chuck_facts.py`.

See `coding_take-home.md` for the original assignment brief.
