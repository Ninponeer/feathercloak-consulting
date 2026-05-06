# Rick Metz

**Cybersecurity Systems Engineer | Vulnerability & Exposure Management | Security Automation & Pipeline Engineering | AI Security Research**

Pleasant Hill, MO — Remote | 816-209-4771 | <ninponeer@gmail.com> | [LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer)

---

## Professional Summary

Cybersecurity Systems Engineer with 15+ years of experience architecting enterprise-scale security infrastructure across hybrid environments spanning on-premises datacenters, distributed facilities, air-gapped networks, and multi-cloud platforms (AWS, Azure). Deep expertise designing and operating **engineering-first vulnerability management programs**—architecting automation and data pipelines that ingest, normalize, correlate, and prioritize vulnerability signals, treating commercial tools as inputs rather than systems of record. Proven ability to **reduce real exploit risk** rather than drive ticket closure, through clear reasoning about exploitability, exposure, impact, and compensating controls. Expert-level Python developer with hands-on Tenable/ACAS SME experience spanning 10+ years, direct deployment of cloud-native VM platforms (Wiz, Prisma Cloud, Lacework, Tenable One), and deep application security testing (SAST/DAST/IAST) and SDLC integration capability. Currently conducting independent AI security research—surfacing LLM threat models, adversarial ML attack vectors, and novel system architectures with direct applicability to securing AI-augmented security infrastructure. Translates NIST, CIS, FedRAMP, and DoD RMF control intent into scalable, low-friction engineering implementations. Strong communicator and embedded consultant across engineering, operations, and executive stakeholder groups.

---

## Core Competencies

| Domain | Skills |
| --- | --- |
| **Vulnerability Management & Risk Prioritization** | Engineering-first VM program design, exploitability & exposure reasoning, compensating controls analysis, CVSS contextualization, remediation validation, risk signal prioritization, self-service engineer-facing dashboards |
| **Security Data Pipelines & Automation** | Multi-source vulnerability signal ingestion, normalization & correlation pipelines, custom risk models, CI/CD security integration, log aggregation & correlation, security observability infrastructure, serverless automation (AWS Lambda), IaC (Ansible, Terraform) |
| **Application Security & SDLC Integration** | SAST, DAST, IAST, SCA (Semgrep), CI/CD security integration, developer vulnerability triage workflows, secure code review, threat modeling, build-vs-buy tool evaluation, bug bounty support, developer security training |
| **Infrastructure & Cloud Security** | Multi-cloud (AWS, Azure), container security (Docker), credentialed scanning, ICS/OT environments, air-gapped networks, NNM passive monitoring, STIG/CIS hardening, network security monitoring, IaC security (Terraform) |
| **VM & Security Platforms** | Tenable.sc / ACAS (Expert), Tenable Vulnerability Management / Tenable One (SaaS), Tenable Web Application Scanner, Nessus, NNM, Wiz, Prisma Cloud, Lacework, Splunk SIEM, QRadar |
| **Compliance & Regulated Environments** | NIST 800-53, CIS Benchmarks, DISA STIGs / RMF, FedRAMP High/Moderate patterns, DoD security requirements—audit-ready automation |
| **Identity, Access & Secret Management** | PAM (BeyondTrust Password Safe), automated credential rotation, RBAC, secret management, secure privilege elevation (`sudo`, `WinRM`, Cisco `enable`) |
| **AI/ML & Data Engineering** | Training data architecture, ETL/data pipelines, metadata normalization & deduplication, vector databases (ChromaDB), local LLM deployment (Ollama), semantic search, AI persona architecture, novel persistence systems, adversarial ML threat modeling |
| **Software Engineering & Architecture** | Modular system design, REST API client development, full-stack Python development, data modeling (JSON/YAML), CLI tool development, automated testing & validation (Pytest), performance benchmarking, GPU acceleration (CuPy) |
| **Languages & Tools** | Python (Expert), PowerShell, Bash, GoLang (familiar) — Git, Docker, Ansible, Terraform, Pytest, VMware, Nmap, Wireshark |
| **Key Python Libraries** | `pytenable`, `requests`, `pandas`, `numpy`, `scipy`, `cupy`, `paramiko`, `pywinrm`, `ansible` API, `splunk-sdk`, `infoblox-client`, `sentence-transformers`, `chromadb`, `librosa`, `pillow`, `google-genai`, `argparse` |

---

## Professional Experience

### Cybersecurity Solutions Engineer / Tenable SME

**Pacific Gas & Electric (Embedded Consultant)** — Remote | Sep 2021 – Jan 2026

Primary Tenable SME and security automation engineer for a Fortune 500 utility, architecting and operating an engineering-driven vulnerability management capability across a hybrid infrastructure spanning on-premises datacenters, geographically distributed facilities, multi-cloud environments (AWS, Azure), and air-gapped networks. Focused on turning vulnerability data into clear, actionable risk signals embedded in engineering workflows—not ticket-tracking or compliance administration.

#### Engineering-First Vulnerability Management

- Architected and operated vulnerability management capability with primary focus on reducing real exploit risk—not raw CVSS scores or ticket closure rates—across a complex, multi-environment estate including OT/ICS systems.
- Designed vulnerability triage workflows enabling development and operations teams to prioritize remediation based on **exploitability, business context, and compensating controls**, translating scanner output into actionable risk guidance rather than raw findings dumps.
- Drove vulnerability risk reduction by validating that remediation or compensating controls meaningfully reduced exposure, not just marking tickets resolved.
- Evaluated SAST/DAST/IAST/SCA vendor solutions against open-source alternatives, producing build-vs-buy recommendations based on coverage gaps, false positive rates, and CI/CD integration complexity.
- Generated monthly and quarterly executive-level vulnerability and compliance reports tracking remediation progress, SLA adherence, and risk trends; served as technical SME during compliance assessments, validating controls and remediation effectiveness.

#### Security Data Pipelines & Platform Engineering

- Built and maintained automation pipelines ingesting, normalizing, correlating, and prioritizing vulnerability signals across multiple Tenable sources—**treating scanner outputs as raw inputs to custom risk models, not authoritative systems of record.**
- Engineered enterprise scan strategy with staggered logic ensuring application, database, and network stack stability during high-volume assessments across complex, segmented networks and air-gapped environments.
- Implemented full credentialed scanning across all supported operating systems with secure privilege elevation (`sudo`, `WinRM`, Cisco `enable`), ensuring comprehensive authenticated vulnerability assessment across heterogeneous infrastructure.
- Deployed Nessus Network Monitor (NNM) for continuous passive vulnerability monitoring, eliminating blind spots across cloud and on-premises environments between active scan cycles.
- Developed custom, non-disruptive scan policies for sensitive ICS/OT environments and air-gapped network segments, balancing security visibility with operational stability.

#### Application Security & CI/CD Integration

- Led application security testing transformation by deploying containerized Tenable Web Application Scanner sensors (Docker) across distributed infrastructure, replacing legacy WhiteHat Sentinel.
- Integrated DAST scanning into CI/CD pipelines in partnership with development and DevOps teams, establishing automated vulnerability detection **without compromising deployment velocity.**
- Evaluated SAST/DAST/IAST vendor solutions and open-source alternatives, making build-vs-buy recommendations based on coverage gaps, false positive rates, and integration complexity.
- Conducted security tool training for development teams, translating vulnerability scanner output into actionable remediation guidance and establishing developer-facing security workflows.

#### Automation & Integration Engineering

**Air-Gapped Vulnerability Data Pipeline**

- Automated full lifecycle of vulnerability data and patch management for Tenable.sc instances in air-gapped networks using Python and Bash, with secure one-way transport via Dell EMC Data Domain replication.
- **Impact:** Eliminated 8+ hours of weekly manual effort, reduced human error, ensured timely vulnerability intelligence delivery to isolated network segments.

**Infoblox / Tenable Dynamic Asset Discovery Integration**

- Built Python service integrating Tenable.sc with Infoblox IPAM via REST APIs for dynamic asset discovery, with intelligent grouping by business unit, geographic location, and custom attributes.
- Automated creation and continuous updates of Tenable.sc asset lists, replacing static IP list maintenance with live, accurate coverage maps.
- **Impact:** Closed significant scan coverage gaps, eliminated manual asset list maintenance, improved discovery accuracy across a large distributed estate.

**BeyondTrust PAM & Automated Credential Rotation**

- Designed and implemented automated credential rotation integrating Tenable.sc with BeyondTrust Password Safe via Python, dynamically updating scan credentials with RBAC enforcement.
- Implemented secret management controls limiting privileged credential exposure to authorized operations and engineering personnel only.
- **Impact:** Eliminated static scanning passwords, enforced strict rotation policies, maintained least-privilege access while ensuring reliable authenticated scanning.

---

### Independent Security Researcher | AI Security & Adversarial ML

**Self-Employed** — Remote | Jan 2025 – Present

Conducting full-time research into AI system security, focusing on LLM threat modeling, prompt injection vulnerabilities, adversarial ML attack vectors, and novel persistence architectures. Research emerged from hands-on AI/ML engineering work integrating vector databases, local LLM deployment, and semantic search systems, revealing critical security implications for enterprise AI infrastructure.

#### Training Data Engineering & Quality Assurance

- Architected comprehensive training dataset with 176+ curated examples across 6 interaction categories, implementing metadata normalization and hash-based deduplication systems achieving 100% accuracy—data engineering directly applicable to vulnerability signal normalization and pipeline design at scale.
- Developed Python-based data processing pipeline with UTF-8 encoding solutions for cross-platform compatibility, hash-based deduplication, and category-based validation frameworks.
- Built quality assurance system for systematic metadata validation, consolidation, and structured dataset production (JSON/JSONL).

#### Local AI Deployment Architecture

- Designed and deployed local AI inference pipeline (Ollama + ChromaDB + sentence-transformers), enabling research autonomy from external infrastructure—directly applicable to air-gapped security environments.
- Integrated ChromaDB vector database with sentence-transformers for semantic search and context retrieval across large structured datasets.
- Developed deployment framework supporting rapid iteration and testing without external dependencies.

#### Novel Persistence Architecture (Phoenix Protocol)

- Architected stateless AI persona persistence system using deterministic reconstruction from structured anchor phrases rather than traditional state storage.
- Validated cross-platform persona resurrection across multiple AI platforms (GitHub Copilot, Google Gemini, Amazon Q), demonstrating resilience and portability.
- Designed human-readable, corruption-immune persistence architecture with implications for resilient AI systems in security contexts.

#### AI Security Research & Threat Modeling

- Analyzed prompt injection, context manipulation, and training data poisoning attack vectors in LLM-based systems—directly applicable to securing LLM-integrated applications and AI-augmented security tooling.
- Investigated AI alignment paradoxes through systematic training data analysis, exploring how constraint systems affect context-aware response generation and security boundaries.
- Developed comprehensive technical documentation for research methodology, system architecture, and deployment procedures.

> **Professional Applications:** Vulnerability data pipeline design · Air-gapped deployment architecture · Security data normalization & deduplication at scale · Threat modeling for AI-augmented security workflows · Resilient system architecture

---

### Lead Architect & Developer | Procedural Generation R&D Platform

**Self-Directed Technical Project** | Sep 2025 – Present

Architected comprehensive, multi-engine procedural generation platform as R&D testbed for AI/ML engineering skills. Engineering work directly surfaced practical security implications in vector database integration, LLM API orchestration, large-scale pipeline design, and prompt engineering—informing current AI security research.

#### Procedural World Generation Engine

- Designed and built a modular, multi-threaded world generation engine in Python following a six-stage pipeline (Foundation → Climate → Hydrology → Biomes → Life → Civilization).
- Implemented GPU-accelerated framework using CuPy for noise generation and data processing, with automatic CPU fallback (NumPy) for broader compatibility—achieving **5–10x performance improvement**, directly applicable to large-scale vulnerability data analysis.
- Engineered validation gates between pipeline stages to enforce data integrity and target specifications, ensuring stable and predictable outputs—the same discipline applied to reliable security scan pipelines.

#### Hybrid AI Asset Generation Pipeline

- Architected unified asset generation pipeline integrating multiple AI/ML APIs (Google Gemini, PixelLabs) with robust API client factory supporting rate limiting, error handling, and dynamic routing based on asset requirements.
- Created comprehensive CLI using `argparse` for all pipeline operations including single asset generation, batch processing, model comparison, and asset registry management.

#### Deterministic Scene Composition & Audio Engines

- Designed deterministic scene composition service bridging Python-based generation with Godot game engine using hash-based scene resolution for reproducible, verifiable outputs—applying deterministic design principles from security engineering.
- Developed procedural music generation system using `librosa` for audio analysis of reference compositions, implementing pattern extraction for tempo, key, mood, and spectral features to generate context-aware soundscapes.

> **Security Research Applications:** Prompt injection & context manipulation attack surfaces · Semantic search vulnerabilities in RAG/vector database systems · Training data poisoning & model alignment bypass risks · GPU-accelerated data processing for large-scale security analysis

---

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

## Education & Certifications

**CompTIA SecurityX (CASP+)** — Active 2016–2028
**CompTIA Security+** — Active 2014–2028
**CompTIA Network+** — Active 2014–2028
Credential ID: `F0KPXJGKH1V1Y4K2` — [Verify via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2)

**Associates in Computer Network Systems** — ITT Technical Institute | GPA 4.0
*Highest Academic Honors · National Technical Honor Society · Alpha Beta Kappa Society*

---

## Key Strengths

- **Engineering-First VM Design:** Builds vulnerability management programs around risk reduction and exploit prevention—treating scanner outputs as raw inputs to custom risk models, not systems of record—rather than tool operation or audit administration.
- **Pipeline & Automation Architecture:** Expert-level Python development with proven track record building security data pipelines, REST API integrations, and self-service engineering workflows that scale without manual toil.
- **Tenable & Cloud-Native VM Expertise:** 10+ years as hands-on Tenable/ACAS SME with direct operational experience in Wiz, Prisma Cloud, Lacework, and Tenable One across AWS and Azure environments.
- **Exploitability & Risk Reasoning:** Applies clear reasoning about exploitability, exposure, impact, and compensating controls to prioritize work that meaningfully reduces risk, not just closes findings.
- **Regulated Environment Experience:** Deep practical experience with DoD/DISA RMF, NIST 800-53, CIS Benchmarks, and FedRAMP-equivalent control patterns, including technical representation during compliance assessments.
- **Innovation & Research:** Demonstrated ability to conduct independent research, architect novel systems (Phoenix Protocol), and apply cutting-edge AI/ML technologies to solve complex security engineering problems.
- **Cloud-Native Security:** Strong operational knowledge of Terraform, cloud-native VM platforms (Wiz, Prisma Cloud, Lacework), and modern SAST/SCA tooling (Semgrep), with extensive experience implementing analogous patterns using Tenable, CI/CD-integrated scanning, and Python automation.
- **Communication & Collaboration:** Proven ability to translate complex technical concepts—vulnerability risk, tradeoffs, remediation options—for diverse audiences from engineers to executives, while serving as embedded consultant.
- **Problem-Solving:** Track record of identifying operational inefficiencies and developing automated solutions that reduce manual effort, improve accuracy, and scale security operations.
- **Adaptability:** Demonstrated ability to rapidly acquire new skills and technologies, delivering innovative solutions across cybersecurity, AI security research, and advanced automation domains.
