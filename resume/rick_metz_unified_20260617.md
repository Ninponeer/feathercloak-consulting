# Rick Metz

**Vulnerability Management Architect | Remediation Program Lead | Security Automation & Platform Engineering**

Pleasant Hill, MO — Remote | 816-209-4771 | ninponeer@gmail.com | [LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer)

---

## Professional Summary

Senior Cybersecurity Systems Engineer with 15+ years of experience across enterprise, critical infrastructure, and DoD environments, including 10+ years as a hands-on Tenable / ACAS SME. Currently leading a large-scale **vulnerability remediation program** for a Fortune-scale enterprise client — designing governance, prioritization models, data pipelines, and cross-functional execution cadence to drive measurable backlog reduction and risk burn-down across 600+ assets and 900+ critical/high findings.

Builds **engineering-first vulnerability management capabilities**: credentialed coverage, safe scan strategy, threat-informed prioritization (CVSS, VPR, EPSS, CISA KEV, exploitability, asset criticality), remediation validation, formal risk acceptance, and executive reporting. Expert Python developer with deep experience integrating security platforms across hybrid, multi-cloud, air-gapped, and OT/ICS environments. Proven program builder who operationalizes runbooks, TaskORD-style remediation campaigns, SLA matrices, and repeatable workflows aligned to HITRUST CSF, NIST 800-53, CIS, FedRAMP, and DoD RMF. Also conducts independent AI security research — skills directly transferable to vulnerability data normalization, pipeline engineering, and securing LLM-augmented security tooling.

---

## Professional Experience

### Security Engineer / Tenable SME — Remediation Program Lead

**Vaco (Contract Consultant)** — Remote | Mar 2026 – Present

Engaged on a six-month remote contract as Cybersecurity Engineer and Tenable SME for a large enterprise security engineering program. Primary focus: **Tenable One platform stabilization**, root-cause remediation of scan visibility failures, and execution of **Project ARC (Active Remediation Campaign)** — a time-sensitive vulnerability reduction initiative spanning platform engineering, governance design, data-driven remediation tracking, and cross-functional stakeholder coordination.

#### Program Leadership & Governance (Project ARC)

- Designed and launched **Project ARC**, a comprehensive vulnerability remediation program including strategic directive, **TaskORD** repeatable campaign model, **SEV5→SEV1** severity/SLA matrix, structured **risk acceptance governance**, and tagging conventions — aligned to HITRUST CSF and NIST 800-53 (RA-5, SI-2, CM-8, ID.RA, PR.IP, DE.CM, RS.MI).
- Led **TaskORD-001**, the primary remediation campaign: **648 assets**, **977 Critical/High findings** (399 Critical, 578 High), **137 unique plugins**, with **876 findings aged >30 days** at baseline; established filter criteria, asset/vulnerability tagging (`ARC:TaskORD-001`, `SEV`, `Owner`, `PatchWindow`), and weekly/monthly/quarterly reporting cadence.
- Diagnosed and remediated a platform-level misconfiguration — **entire Windows plugin family disabled on agent-based workstation scans** — that masked remediation progress for months; re-enabled plugin dependencies, restoring trustworthy scan data and achieving **48% finding clearance in the first post-fix scan cycle**.
- Separated **~225 true residual remediation findings** from **~209 scan-visibility artifacts**, eliminating artificial risk-acceptance inflation (100+ plugins previously accepted as workaround) and establishing evidence-based remediation workflow.
- Seeded Azure DevOps backlog with **1 Epic, 7 Features, 19 PBIs** enforcing dependency chains (visibility gaps → platform hygiene → exposure quality → leadership review) with Definition of Ready/Done and artifact crosswalks.

#### Risk-Based Prioritization, Data Pipelines & Remediation Validation

- Built repeatable **Python/Jupyter data pipelines** (`arc_runner.py` CLI orchestrator) transforming raw Tenable exports into analysis-ready datasets: normalized cohort filtering, credentialed-scan validation (plugin 19506), Windows authentication evidence (15+ promoted auth plugins), reboot-state correlation (plugin 35453), and stale-agent segmentation (`fresh`/`stale`/`unknown`).
- Owned prioritization model incorporating **CVSS, VPR, CISA KEV, exploit maturity, asset criticality, exposure, business impact, and compensating controls**; cataloged 100+ risk-accepted plugins with structured metadata for governance disposition (rationale, approver, expiration, review cadence).
- Authored **5-tab remediation tracking workbook specification** (Plugin Inventory, Affected Hosts & Remediation Strategy, Summary Metrics, RCA Mapping, Vendor Engagement) with executive summary automation and week-over-week delta tracking for backlog reduction and SLA compliance metrics.

#### Platform Integrations, Runbooks & Cross-Functional Coordination

- Implemented **Tenable One + Microsoft Entra ID SAML SSO** end-to-end: Entra SAML app, SP metadata exchange, group/role claims, auto-provisioning, fallback roles, 10-scenario test plan, and operational runbook.
- Configured **RBAC** using Intune and Microsoft Entra ID SSO, establishing centralized identity-backed access control for the vulnerability management platform.
- Designed **Tenable ↔ Freshservice VMT workflow**: plugin-based remediation ticketing (Host tickets per asset, Plugin tickets per plugin ID), portfolio dashboard KPIs, remediation progress graphs, and business-unit security posture ranking.
- Architected **AWX / Ansible Automation Platform + Uyuni** centralized Linux patch/compliance platform: Tenable-driven remediation triggers, Entra ID RBAC, Salt minion deployment, OpenSCAP/InSpec compliance integration.
- Developed **CMDB/asset intelligence join strategy** across Tenable, SCCM, Intune, and Freshservice with tag-based enrichment (`owner:`, `business_unit:`, `environment:`, `criticality:`) and inventory reconciliation automation (`reconcile_manifest_inventory.py`).
- Partnered with IT operations, endpoint management (SCCM/Intune), and business stakeholders to plan remediation with minimal disruption; documented escalation paths, exception handling, and remediation procedures for steady-state transition.

---

### Cybersecurity Solutions Engineer / Tenable SME

**Pacific Gas & Electric (Embedded Consultant)** — Remote | Sep 2021 – Jan 2026

Primary Tenable SME and security automation engineer for a Fortune 500 utility, architecting and operating an engineering-driven vulnerability management capability across hybrid infrastructure spanning on-premises datacenters, geographically distributed facilities, multi-cloud environments (AWS, Azure), and air-gapped networks. Focused on turning vulnerability data into clear, actionable risk signals embedded in engineering workflows — not ticket-tracking or compliance administration.

#### Vulnerability Management & Platform Engineering

- Architected and operated vulnerability management capability with primary focus on reducing **real exploit risk** — not raw CVSS scores or ticket closure rates — across a complex, multi-environment estate including OT/ICS systems spanning **50,000+ assets**.
- Designed vulnerability triage workflows enabling development and operations teams to prioritize remediation based on **exploitability, business context, and compensating controls**, translating scanner output into actionable risk guidance rather than raw findings dumps.
- Built and maintained automation pipelines ingesting, normalizing, correlating, and prioritizing vulnerability signals across multiple Tenable sources — **treating scanner outputs as raw inputs to custom risk models, not authoritative systems of record.**
- Engineered staggered scan logic and custom, non-disruptive policies for sensitive ICS/OT systems, segmented networks, and air-gapped environments.
- Implemented full credentialed scanning across all supported operating systems with secure privilege elevation (`sudo`, `WinRM`, Cisco `enable`), ensuring comprehensive authenticated vulnerability assessment across heterogeneous infrastructure.
- Deployed Nessus Network Monitor (NNM) for continuous passive vulnerability monitoring, eliminating blind spots across cloud and on-premises environments between active scan cycles.
- Produced executive vulnerability and compliance reporting; represented technical controls during assessments; trained development teams on actionable remediation workflows and risk burn-down tracking.

#### Security Automation & Integration Engineering

**Air-Gapped Vulnerability Data Pipeline**
- Automated full lifecycle of vulnerability data and patch management for air-gapped Tenable.sc instances using Python and Bash with secure one-way transport via Dell EMC Data Domain replication.
- **Impact:** Eliminated **8+ hours of weekly manual effort**, reduced human error, ensured timely vulnerability intelligence delivery to isolated segments.

**Infoblox / Tenable Dynamic Asset Discovery**
- Built Python service integrating Tenable.sc with Infoblox IPAM via REST APIs for dynamic asset discovery, with intelligent grouping by business unit, geographic location, and custom attributes.
- Automated creation and continuous updates of Tenable.sc asset lists, replacing static IP maintenance with live coverage maps.
- **Impact:** Closed significant scan coverage gaps, eliminated manual asset list maintenance, improved discovery accuracy across a large distributed estate.

**BeyondTrust PAM & Automated Credential Rotation**
- Designed and implemented automated credential rotation integrating Tenable.sc with BeyondTrust Password Safe via Python, dynamically updating scan credentials with RBAC enforcement.
- **Impact:** Eliminated static scanning passwords, enforced strict rotation policies, maintained least-privilege access while ensuring reliable authenticated scanning.

#### Application Security & Advisory

- Led deployment of containerized Tenable Web Application Scanner sensors across distributed infrastructure, replacing legacy WhiteHat Sentinel.
- Integrated **DAST** scanning into CI/CD pipelines in partnership with development and DevOps teams, establishing automated vulnerability detection without compromising deployment velocity.
- Evaluated **SAST, DAST, IAST, and SCA** solutions against open-source alternatives, producing build-vs-buy recommendations based on coverage, false-positive rates, and integration complexity.
- Coordinated cross-functional remediation execution with application owners, system administrators, and distributed operations teams; validated remediation closure accuracy through structured rescanning and reporting.

---

### USMC – KCITC Datacenter

Kansas City, MO | Jun 2014 – Jul 2021

#### Cybersecurity Systems Engineer / ACAS & Tenable SME

*Aug 2016 – Jul 2021*

- Led deployment, maintenance, and administration of all cybersecurity systems including ACAS (Tenable.sc, Nessus, NNM) and Splunk SIEM for mission-critical DoD datacenter environments supporting classified and unclassified networks.
- Architected and maintained vulnerability management infrastructure ensuring compliance with DoD security requirements (DISA STIGs, RMF) — directly analogous to FedRAMP High/Moderate control environments.
- Developed Ansible content to automate STIG baseline configurations and security control enforcement at scale, producing audit-ready evidence through automation rather than manual administration.
- Facilitated automation of network discovery scan workflows using Nmap, PowerShell, and Python, improving asset visibility and scan coverage across complex, segmented DoD networks.

#### Cybersecurity Analyst Sr / ACAS Engineer

*Apr 2015 – Aug 2016*

- Owned the ACAS platform and underlying RHEL infrastructure, designing and maintaining comprehensive vulnerability and compliance scan policies in Tenable Security Center.
- Collaborated with system administrators and application owners to prioritize and remediate critical vulnerabilities based on exploitability and operational context.
- Generated executive-level reports and metrics on vulnerability trends, remediation progress, MTTR, and risk reduction.

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
| **Remediation Program Leadership** | Backlog burn-down, TaskORD/campaign design, SLA matrices, cross-functional & distributed team coordination, executive reporting, lessons-learned capture, steady-state transition planning |
| **Vulnerability & Exposure Management** | Engineering-first VM program design, credentialed scanning, safe scan strategy, exploitability & exposure reasoning, CVSS/VPR contextualization, EPSS & CISA KEV triage, remediation validation, formal risk acceptance |
| **Security Automation & Platform Engineering** | Python (`pytenable`, pandas, Jupyter), REST API integrations, vulnerability data pipelines, CLI orchestration, Freshservice VMT workflow design, Ansible, AWX/AAP, Uyuni, Terraform, Docker |
| **Application & Cloud Security** | AWS, Azure, SAST, DAST, IAST, SCA, CI/CD security integration, containerized assessment sensors, threat modeling, build-vs-buy evaluation |
| **Security Platforms** | Tenable One, Tenable.sc / ACAS, Tenable VM, Nessus Agents, NNM, Tenable WAS, Wiz, Prisma Cloud, Lacework, Splunk SIEM, QRadar |
| **Identity, Access & Secrets** | Microsoft Entra ID SAML SSO, Intune, RBAC, BeyondTrust Password Safe, automated credential rotation, secret management, secure privilege elevation |
| **Regulated & Sensitive Environments** | HITRUST CSF, DoD RMF, DISA STIGs, NIST 800-53, NIST CSF, CIS Benchmarks, FedRAMP patterns, OT/ICS, air-gapped networks, audit-ready automation |
| **AI / ML & Data Engineering** | LLM threat modeling, adversarial ML, RAG/vector databases, local inference, metadata normalization, deduplication, semantic search, GPU acceleration |
| **Languages & Tools** | Python (Expert), PowerShell, Bash, Go (familiar), Git, Pytest, Azure DevOps Boards, VMware, Nmap, Wireshark |

---

## Selected Research & Technical Projects

### AI Security & Adversarial ML Research

**Independent Research** | Jan 2025 – Present

- Analyzing prompt injection, context manipulation, training data poisoning, and RAG/vector-database attack surfaces in LLM-integrated systems.
- Built local inference and semantic-search environment using Ollama, ChromaDB, and sentence-transformers for repeatable offline research.
- Developed Python data pipelines for metadata normalization, hash-based deduplication, validation, and structured JSON/JSONL dataset production — patterns directly applicable to vulnerability data normalization at scale.
- Designed deterministic, file-based context-reconstruction architecture (Phoenix Protocol) to study portability, integrity, and security boundaries across AI platforms.

### Systems Engineering R&D Platform

**Self-Directed Technical Project** | Sep 2025 – Present

- Built modular, multi-threaded Python procedural-generation pipeline with validation gates between stages and automatic NumPy CPU fallback for GPU-accelerated CuPy workloads; achieved **5–10x performance improvement** while preserving deterministic, testable outputs.
- Architected multi-provider AI API client factory with rate limiting, error handling, dynamic routing, and CLI-driven batch operations.

---

## Education & Certifications

**CompTIA SecurityX (CASP+)** — Active 2016–2028  
**CompTIA Security+** — Active 2014–2028  
**CompTIA Network+** — Active 2014–2028  
Credential ID: `F0KPXJGKH1V1Y4K2` — [Verify via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2)

**Associates in Computer Network Systems** — ITT Technical Institute | GPA 4.0  
*Highest Academic Honors · National Technical Honor Society · Alpha Beta Kappa Society*

---

*References and detailed project artifacts (governance frameworks, automation samples, integration designs) available upon request.*