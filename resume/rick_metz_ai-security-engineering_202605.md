# Rick Metz

**AI Security Researcher & Cybersecurity Systems Engineer | LLM / Agent Security | Security Automation | Applied AI Engineering**

Pleasant Hill, MO — Remote | 816-209-4771 | <ninponeer@gmail.com> | [LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer)

---

## Professional Summary

AI Security Researcher and Cybersecurity Systems Engineer with 15+ years of experience securing enterprise, critical-infrastructure, and DoD environments. Builds practical security methods, prototypes, and automation for emerging AI risks including prompt injection, context manipulation, data poisoning, agent trust boundaries, and RAG / vector-database attack surfaces. Developed an alpha LLM vulnerability-assessment framework, a vendor-neutral model-targeting specification, local evaluation environments, and agentic cloud-security tooling. Expert Python developer with deep experience translating ambiguous security problems into repeatable engineering systems, from AI evaluation prototypes to enterprise vulnerability pipelines, API integrations, and remediation workflows across hybrid, multi-cloud, air-gapped, and OT / ICS environments.

---

## Applied AI Security & Engineering

### Auralith — LLM Vulnerability Assessment Framework

**Independent R&D** | Mar 2026 – Present

- Designed and prototyped an alpha LLM vulnerability-assessment framework applying established vulnerability-management patterns to models and agentic applications: target enumeration, scan policies, severity taxonomy, evaluation probes, and mitigation-oriented reporting.
- Defined **LLMPE v1.0**, a vendor-neutral specification for identifying LLM platforms and deployment contexts, plus JSON schemas for probes and Nessus-style assessment policies.
- Built the initial engine architecture around probe execution, wildcard target matching, adapter registration, CLI-driven scanning, and explicit safety profiles for production, pre-deployment, and isolated research environments.
- Validated Ollama and GitHub Models adapters; scaffolded OpenAI and Anthropic adapters for further validation.

### Agentic Cloud Security Prototype

**Independent Prototype** | 2026

- Built a tool-calling LangChain agent backed by a local Ollama model and Python tools for AWS security inspection: S3 ACL and object enumeration, EC2 instance lookup, and IAM attached-policy analysis.
- Created Moto-backed mock AWS resources, smoke tests, CLI runners, and deterministic offline verification paths so the prototype could be exercised without live cloud credentials.

### AI Security & Resilient Context Architecture

**Independent Research** | Jan 2025 – Present

- Analyzing prompt injection, context manipulation, training-data poisoning, agent abuse, and secure RAG / vector-database design in LLM-integrated systems.
- Built a local inference and semantic-search lab using Ollama, ChromaDB, and sentence-transformers for repeatable offline research.
- Developed Python pipelines for metadata normalization, hash-based deduplication, validation, and structured JSON / JSONL dataset production.
- Designed and documented **Phoenix Protocol**, a deterministic file-based context-reconstruction architecture for studying portability, integrity, trust boundaries, and cross-platform behavior.

### Accelerated Systems Engineering R&D Platform

**Self-Directed Technical Project** | Sep 2025 – Present

- Built a modular, multi-threaded Python data-processing pipeline with validation gates between stages and automatic NumPy CPU fallback for GPU-accelerated CuPy workloads.
- Achieved **5–10x performance improvement** while preserving deterministic, testable outputs.
- Architected a multi-provider AI API client factory with rate limiting, error handling, dynamic routing, and CLI-driven batch operations.

---

## Professional Experience

### Security Engineer / Tenable SME

**Vaco (Contract Consultant)** — Remote | Mar 2026 – Present

Engaged on a six-month remote contract to support an enterprise security engineering program, with primary focus on Tenable platform stabilization, cleanup, and an extensive vulnerability remediation campaign. Current work spans platform engineering, identity-backed access control, risk-based triage workflow design, and centralized Linux infrastructure management architecture.

- Executing Tenable platform stabilization and cleanup during an extensive vulnerability remediation campaign, with focus on repeatable scanning, triage, and remediation practices.
- Configured and implemented RBAC using Intune and Microsoft Entra ID SSO, establishing centralized identity-backed access control for the vulnerability management platform.
- Designing an MVP integration with Freshservice to route vulnerabilities past SLA and emerging threats, including CISA Known Exploited Vulnerabilities (KEV) and other risk factors, into actionable triage workflows.
- Designing centralized management architecture for Linux infrastructure using AWX / Ansible Automation Platform (AAP) and Uyuni to support repeatable configuration and remediation operations.

---

### Cybersecurity Solutions Engineer / Tenable SME

**Pacific Gas & Electric (Embedded Consultant)** — Remote | Sep 2021 – Jan 2026

Primary Tenable SME and security automation engineer for a Fortune 500 utility, architecting and operating an engineering-driven vulnerability management capability across a hybrid infrastructure spanning on-premises datacenters, geographically distributed facilities, multi-cloud environments (AWS, Azure), and air-gapped networks. Focused on turning vulnerability data into clear, actionable risk signals embedded in engineering workflows—not ticket-tracking or compliance administration.

#### Vulnerability Management & Platform Engineering

- Architected and operated vulnerability management capability with primary focus on reducing real exploit risk—not raw CVSS scores or ticket closure rates—across a complex, multi-environment estate including OT/ICS systems.
- Designed vulnerability triage workflows enabling development and operations teams to prioritize remediation based on **exploitability, business context, and compensating controls**, translating scanner output into actionable risk guidance rather than raw findings dumps.
- Built and maintained automation pipelines ingesting, normalizing, correlating, and prioritizing vulnerability signals across multiple Tenable sources—**treating scanner outputs as raw inputs to custom risk models, not authoritative systems of record.**
- Engineered staggered scan logic and custom, non-disruptive policies for sensitive ICS/OT systems, segmented networks, and air-gapped environments.
- Implemented full credentialed scanning across all supported operating systems with secure privilege elevation (`sudo`, `WinRM`, Cisco `enable`), ensuring comprehensive authenticated vulnerability assessment across heterogeneous infrastructure.
- Deployed Nessus Network Monitor (NNM) for continuous passive vulnerability monitoring, eliminating blind spots across cloud and on-premises environments between active scan cycles.

#### Security Automation & Integration Engineering

- Automated the vulnerability data and patch-management lifecycle for air-gapped Tenable.sc instances using Python and Bash with secure one-way transport, eliminating **8+ hours of weekly manual effort**.
- Built Python service integrating Tenable.sc with Infoblox IPAM via REST APIs for dynamic asset discovery, with intelligent grouping by business unit, geographic location, and custom attributes.
- Automated creation and continuous updates of Tenable.sc asset lists, replacing static IP maintenance with live coverage maps and closing significant visibility gaps.
- Designed and implemented BeyondTrust Password Safe integration for automated credential rotation, eliminating static scanning passwords while preserving least-privilege access.

#### Application Security & Advisory

- Led deployment of containerized Tenable Web Application Scanner sensors across distributed infrastructure, replacing legacy WhiteHat Sentinel.
- Integrated DAST scanning into CI/CD pipelines in partnership with development and DevOps teams, establishing automated vulnerability detection without compromising deployment velocity.
- Evaluated SAST, DAST, IAST, and SCA solutions against open-source alternatives, producing build-vs-buy recommendations based on coverage, false-positive rates, and integration complexity.
- Produced executive vulnerability and compliance reporting, represented technical controls during assessments, and trained development teams on actionable remediation workflows.

### USMC – KCITC Datacenter

Kansas City, MO | Jun 2014 – Jul 2021

#### Cybersecurity Systems Engineer / ACAS & Tenable SME

*Aug 2016 – Jul 2021*

- Led deployment, maintenance, and administration of all cybersecurity systems including ACAS (Tenable.sc, Nessus, NNM) and Splunk SIEM for mission-critical DoD datacenter environments supporting classified and unclassified networks.
- Architected and maintained vulnerability management infrastructure ensuring compliance with DoD security requirements (DISA STIGs, RMF)—directly analogous to FedRAMP High/Moderate control environments.
- Developed Ansible content to automate STIG baseline configurations and security control enforcement at scale, producing audit-ready evidence through automation rather than manual administration.
- Facilitated automation of network discovery scan workflows using Nmap, PowerShell, and Python, improving asset visibility and scan coverage across complex, segmented DoD networks.

#### Cybersecurity Analyst Sr / ACAS Engineer

*Apr 2015 – Aug 2016*

- Owned the ACAS platform and underlying RHEL infrastructure, designing and maintaining comprehensive vulnerability and compliance scan policies in Tenable Security Center.
- Collaborated with system administrators and application owners to prioritize and remediate critical vulnerabilities based on exploitability and operational context.
- Generated executive-level reports and metrics on vulnerability trends, remediation progress, and risk reduction.

#### Software Administrator & Application Engineer

*Jun 2014 – Apr 2015*

- Developed foundational automation capabilities using PowerShell for system information retrieval and administrative task automation, establishing the automation-first engineering mindset central to all subsequent security engineering work.

---

## Earlier Career

**Tier II Customer Support / Application Systems Analyst I** — ScriptPro, Mission, KS | 2011–2014
Tier 2 support for robotics pharmacy systems (Windows NT/XP/7, Server 2003/2008); Cisco ASA/PIX firewall and network switch installation and configuration; SQL database maintenance and interface data extraction rules.

**Production Support Analyst** — Cerner, Kansas City, MO | 2010–2011
Level 2 support for Cerner healthcare software (PharmNET, PathNET, XRPrint Services); CCL/SQL database operations in Cerner Millennium environments.

---

## Core Competencies

| Domain | Skills |
| --- | --- |
| **AI Security & Model Risk** | LLM and agent security, prompt injection, context manipulation, training-data poisoning, agent abuse, secure RAG, vector-database attack surfaces, trust-boundary analysis |
| **AI Evaluation & Prototype Engineering** | LLM evaluation probes, assessment policies, severity taxonomies, target enumeration, adapter architecture, CLI tooling, safety profiles, mitigation-oriented reporting |
| **AI / ML & Data Tooling** | Ollama, ChromaDB, sentence-transformers, LangChain, Pandas, NumPy, CuPy, JSON / JSONL pipelines, metadata normalization, deduplication, semantic search |
| **Cybersecurity Research & Defense** | Threat modeling, vulnerability discovery, risk prioritization, secure-by-design recommendations, network defense, SIEM correlation logic, remediation automation |
| **Vulnerability & Exposure Management** | Engineering-first VM program design, credentialed scanning, safe scan strategy, exploitability & exposure reasoning, CISA KEV & emerging-threat triage, remediation validation |
| **Application, Cloud & Infrastructure Security** | AWS, Azure, SAST, DAST, IAST, SCA, CI/CD security integration, Docker, Terraform, Ansible, AWX / AAP, Uyuni, OT / ICS systems, air-gapped networks |
| **Security Platforms** | Tenable.sc / ACAS, Tenable Vulnerability Management / Tenable One, Nessus, NNM, Tenable Web Application Scanner, Wiz, Prisma Cloud, Lacework, Splunk SIEM, QRadar |
| **Languages & Tools** | Python (Expert), PowerShell, Bash, Go (familiar), Git, Pytest, Nmap, Wireshark |

---

## Education & Certifications

**CompTIA SecurityX (CASP+)** — Active 2016–2028
**CompTIA Security+** — Active 2014–2028
**CompTIA Network+** — Active 2014–2028
Credential ID: `F0KPXJGKH1V1Y4K2` — [Verify via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2)

**Associates in Computer Network Systems** — ITT Technical Institute | GPA 4.0
*Highest Academic Honors · National Technical Honor Society · Alpha Beta Kappa Society*
