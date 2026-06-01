# Rick Metz

**Cybersecurity Systems Engineer | Vulnerability & Exposure Management | Security Automation & Platform Engineering**

Pleasant Hill, MO — Remote | 816-209-4771 | <ninponeer@gmail.com> | [LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer)

---

## Professional Summary

Cybersecurity Systems Engineer with 15+ years of experience across enterprise, critical infrastructure, and DoD environments, including 10+ years as a hands-on Tenable / ACAS SME. Currently engaged as a remote Security Engineer supporting Tenable platform stabilization, cleanup, and an extensive vulnerability remediation campaign. Builds **engineering-first vulnerability management capabilities**: credentialed coverage, safe scan strategy, data pipelines, automation, and remediation prioritization grounded in exploitability, exposure, business impact, and compensating controls. Expert Python developer with deep experience integrating security platforms across hybrid, multi-cloud, air-gapped, and OT / ICS environments. Translates NIST, CIS, FedRAMP, and DoD RMF control intent into scalable engineering practices. Also conducts independent AI security research focused on LLM threat models and resilient system architecture.

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
| **Vulnerability & Exposure Management** | Engineering-first VM program design, credentialed scanning, safe scan strategy, exploitability & exposure reasoning, CVSS contextualization, CISA KEV & emerging-threat triage, remediation validation |
| **Security Automation & Platform Engineering** | Python automation, REST API integrations, vulnerability data pipelines, Freshservice workflow design, Ansible, AWX / AAP, Uyuni, Terraform, Docker |
| **Application & Cloud Security** | AWS, Azure, SAST, DAST, IAST, SCA, CI/CD security integration, containerized assessment sensors, threat modeling, build-vs-buy evaluation |
| **Security Platforms** | Tenable.sc / ACAS, Tenable Vulnerability Management / Tenable One, Nessus, NNM, Tenable Web Application Scanner, Wiz, Prisma Cloud, Lacework, Splunk SIEM, QRadar |
| **Identity, Access & Secrets** | Microsoft Entra ID SSO, Intune, RBAC, BeyondTrust Password Safe, automated credential rotation, secret management, secure privilege elevation |
| **Regulated & Sensitive Environments** | DoD RMF, DISA STIGs, NIST 800-53, CIS Benchmarks, FedRAMP patterns, OT / ICS systems, air-gapped networks, audit-ready automation |
| **AI / ML & Data Engineering** | LLM threat modeling, adversarial ML, RAG / vector databases, local inference, metadata normalization, deduplication, semantic search, GPU acceleration |
| **Languages & Tools** | Python (Expert), PowerShell, Bash, Go (familiar), Git, Pytest, VMware, Nmap, Wireshark |

---

## Selected Research & Technical Projects

### AI Security & Adversarial ML Research

**Independent Research** | Jan 2025 – Present

- Analyzing prompt injection, context manipulation, training data poisoning, and RAG / vector-database attack surfaces in LLM-integrated systems.
- Built a local inference and semantic-search environment using Ollama, ChromaDB, and sentence-transformers for repeatable offline research.
- Developed Python data pipelines for metadata normalization, hash-based deduplication, validation, and structured JSON / JSONL dataset production.
- Designed and documented a deterministic, file-based context-reconstruction architecture to study portability, integrity, and security boundaries across AI platforms.

### Systems Engineering R&D Platform

**Self-Directed Technical Project** | Sep 2025 – Present

- Built a modular, multi-threaded Python procedural-generation pipeline with validation gates between stages and automatic NumPy CPU fallback for GPU-accelerated CuPy workloads.
- Achieved **5–10x performance improvement** in data-processing workloads while preserving deterministic, testable outputs.
- Architected a multi-provider AI API client factory with rate limiting, error handling, dynamic routing, and CLI-driven batch operations.

---

## Education & Certifications

**CompTIA SecurityX (CASP+)** — Active 2016–2028
**CompTIA Security+** — Active 2014–2028
**CompTIA Network+** — Active 2014–2028
Credential ID: `F0KPXJGKH1V1Y4K2` — [Verify via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2)

**Associates in Computer Network Systems** — ITT Technical Institute | GPA 4.0
*Highest Academic Honors · National Technical Honor Society · Alpha Beta Kappa Society*
