# Rick Metz

**Senior Exposure Management Engineer | Continuous Threat Exposure Management (CTEM), Attack Surface & Vulnerability Systems Integration**
Pleasant Hill, MO | Remote (U.S. Citizen) | 816-209-4771 | ninponeer@gmail.com
[LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer) | [Credly](https://www.credly.com/users/rick-metz)

---

## Professional Summary

Senior exposure management and infrastructure security engineer with 15+ years architecting enterprise vulnerability management, continuous threat exposure management (CTEM), and security systems integration across critical-infrastructure utilities, DoD enclaves, enterprise datacenters, and modern cloud platforms. Deep technical practice aggregating disparate vulnerability, configuration, and attack surface data sources into unified exposure posture frameworks with an automation-first bias toward removing manual operational overhead.

Hands-on across the full lifecycle of enterprise exposure reduction: architecting credentialed and passive discovery across 50,000+ distributed assets, engineering REST API data ingestion pipelines, establishing dynamic asset categorization and tagging taxonomies, and driving remediation workflows to sustain zero findings past SLA. Deep technical expertise across the Tenable ecosystem (Tenable One Exposure Management, Tenable Lumin Cyber Exposure Score, Tenable.sc, Nessus, Nessus Network Monitor passive ASM), External Attack Surface Management (EASM), and SQL/Python data diagnostic pipelines. Proven record collaborating across infrastructure, application, and compliance stakeholders to diagnose telemetry discrepancies, troubleshoot scanner infrastructure, and communicate actionable exposure risk. Holds CompTIA SecurityX (CASP+).

---

## Core Competencies

| Domain | Skills |
| --- | --- |
| Exposure Management & CTEM (End to End) | Continuous Threat Exposure Management (CTEM) program design, exposure lifecycle governance, attack path analysis, Cyber Exposure Score (CES) tracking, risk-based prioritization, severity/SLA matrices, exception and risk-acceptance workflows, remediation campaigns, executive exposure dashboards, backlog burn-down |
| Attack Surface Management (ASM / EASM) | External and internal attack surface mapping, Nessus Network Monitor (passive NDR/ASM), blind-spot elimination, Cloud Security Posture Management (CSPM), CIEM alignment, network segmentation (VLANs, enclaves, trust zones, ACLs), zero-public-egress topologies, OT/ICS safe-scan exposure assessments |
| Systems Integration & Data Ingestion | Building automated ingestion pipelines connecting distributed vulnerability and exposure data sources via REST APIs; custom Python API toolkits (pytenable, requests, asyncio); serverless Azure Functions for log pull-and-normalize ETL; webhook and event-driven telemetry aggregation |
| Exposure Tooling & Scanning Platforms | Tenable One (Exposure Management Platform), Tenable Lumin, Tenable.sc / ACAS, Nessus, Nessus Network Monitor, Tenable Web Application Scanning; containerized security sensors; scanner deployment, capacity planning, and operational troubleshooting; SAST / DAST / SCA evaluation and CI/CD security gating |
| Asset Discovery, Tagging & Governance | Dynamic asset categorization and tagging strategies, Infoblox REST API IPAM synchronization, CMDB/asset reconciliation, ownership attribution, business-unit grouping, critical asset weighting, stale-agent segmentation, and multi-cloud inventory normalization |
| SQL Diagnostics & Data Pipeline Engineering | Advanced SQL and data querying diagnostics, Jupyter/pandas analytical pipelines converting raw scanner exports into normalized, analysis-ready datasets (cohort filtering, credentialed-scan validation, authentication evidence, reboot-state correlation, exposure trending) |
| Identity, Secrets & Credential Hygiene | BeyondTrust Password Safe automated privileged credential rotation across Linux and Windows fleets, PAM, secret management in distributed workflows, service-account scoping, mTLS, RBAC, SAML SSO with just-in-time provisioning (Tenable One + Entra ID), secure privilege elevation (sudo, WinRM) |
| Detection, Telemetry & SIEM | SIEM pipeline engineering (Splunk, Trellix Helix, Microsoft Sentinel, QRadar), log source onboarding and normalization, correlation rules and dashboards, audit-trail integrity, Microsoft Purview (sensitivity labels, auto-labeling, DLP rule design) |
| Governance, Compliance & Frameworks | NIST Cybersecurity Framework (CSF), NIST 800-53 (RA-5, SI-2, CM-8, ID.RA, DE.CM, RS.MI), CIS Critical Security Controls, ISO/IEC 27001, HITRUST CSF, DoD RMF, DISA STIG / SRG, IAVM, POA&M, Federal Reserve and banking regulatory compliance alignment |

---

## Professional Experience

### Senior Exposure Management Engineer / Tenable SME | Remediation Program Lead
**Vaco (Contract Consultant), US Anesthesia Partners (USAP)** | Remote | Mar 2026 – Present
*Exposure management and security systems integration for a specialized healthcare organization: ~3,000 managed assets across a hybrid, multi-region footprint on a strictly Microsoft/Azure stack with Cisco network infrastructure.*

* **Exposure Platform Stabilization & Ingestion:** inherited a degraded Tenable deployment with severe telemetry ingestion gaps; diagnosed and resolved scanner engine misconfigurations, restored reliable exposure data ingestion, and re-established executive confidence in organizational risk metrics.
* **CTEM & Remediation Program Architecture:** designed the end-to-end continuous exposure remediation program from scratch (strategic directive, campaign model, severity/SLA matrix, risk-acceptance workflow, and enterprise tagging standards); drove an initial campaign against an inherited Critical/High backlog breached past SLA, remediating ~1,000 vulnerabilities in ~30 days and sustaining a zero-breach posture thereafter.
* **API Integration & Automated Triage:** authored a production-grade Python Tenable API toolkit and built an automated daily exposure triage workbook that ingests scanner telemetry and generates prioritized remediation queues for platform teams, serving as the foundational mechanism sustaining the zero-findings-past-SLA state.
* **SQL & Analytical Data Pipelines:** engineered Python/Jupyter data pipelines utilizing pandas and SQL queries to normalize raw scanner exports into analysis-ready exposure datasets, performing cohort filtering, credentialed-scan validation, authentication evidence auditing, reboot-state correlation, and stale-agent segmentation.
* **Asset Discovery & Tagging Governance:** established comprehensive discovery scanning across all managed subnets and VLANs, implementing full credentialed scanning across supported compute and Cisco network infrastructure; developed dynamic asset tagging taxonomies mapping business unit ownership and criticality weighting.
* **Security Telemetry Ingestion (Argus Pipeline):** authored a serverless Python Azure Function in ~6 days to resolve an urgent SecOps visibility gap on WorkDay SaaS audit logs lacking native push feeds; built during an active phishing campaign with network probing, configuring VNet integration, Private Endpoints, NSGs, and zero public internet egress as the organization's reference pattern for SaaS log ingestion and normalization.
* **Identity & Exposure Access Integration:** implemented Tenable One SAML SSO with Microsoft Entra ID end to end, configuring just-in-time user provisioning and role-based access control (RBAC) to eliminate manual account management.
* **Detection & Posture Telemetry:** stabilized Trellix Helix telemetry ingestion and partnered with security engineering to pilot Microsoft Sentinel; redesigned conflicting legacy sensitivity-labeling and DLP rule sets across Microsoft Purview to resolve audit findings.
* **Compliance Metrics & Knowledge Transfer:** generated technical exposure metrics and artifact packages satisfying HITRUST assessment requirements; mentored SecOps analysts on Tenable platform troubleshooting across 30+ business days and delivered full technical documentation for all API tools and ingestion pipelines.

### Cybersecurity Solutions Engineer / Senior Exposure Management SME | Primary Program Architect
**Pacific Gas & Electric** | Remote | Sep 2021 – Jan 2026
*Embedded security consultant via World Wide Technology, with MatchPoint and IS3 Solutions as delivery partners. Primary Tenable SME for a Fortune 500 utility: continuous exposure management and attack surface reduction across on-premises datacenters, distributed substations, multi-cloud (AWS, Azure), air-gapped enclaves, and OT/ICS, spanning 50,000+ assets.*

* **Enterprise Exposure Mapping & Posture Assessment:** mapped the complete attack surface and security posture of a massive, distributed critical-infrastructure environment; conducted systematic gap analyses on previously unscanned address space, engineering custom active scan policies and passive monitoring to eliminate organizational visibility blind spots.
* **Automated Asset Discovery & Tagging (Infoblox REST API):** engineered a Python integration service querying the Infoblox REST API to automatically enumerate enterprise subnets and network containers, classify assets by business unit and geographic site, and dynamically populate Tenable.sc asset lists, replacing error-prone static IP tracking with automated inventory synchronization.
* **Passive Attack Surface Management (NNM):** deployed and managed Nessus Network Monitor (NNM) across enterprise perimeters for continuous passive attack surface discovery, identifying unmanaged devices, shadow IT systems, and unauthorized cross-zone communications without generating disruptive network traffic.
* **Cross-Boundary Telemetry Ingestion & Diode Transport:** built automated Python and Bash data pipeline suites staging, validating, and transferring Tenable plugins and SC feeds through DMZ data diodes into air-gapped enclaves, then extracting and centralizing isolated scan telemetry back into corporate reporting dashboards, eliminating 8+ hours of weekly manual operations.
* **Enterprise Scanning Architecture & Operational Tuning:** architected staggered scanning schedules decoupling application, database, and core network tiers to guarantee critical infrastructure availability during large-scale exposure assessments; diagnosed scanner connectivity bottlenecks and tuned engine concurrency.
* **Credentialed Exposure Scanning & Secrets Management:** integrated BeyondTrust Password Safe with Tenable.sc via a custom Python service that programmatically retrieves automatically rotated credentials to update SSH and SMB scan targets, eliminating scan failures from credential expiration.
* **OT/ICS Safe Exposure Assessments:** engineered tailored, non-disruptive exposure evaluation policies across industrial control systems and supervisory networks, delivering actionable vulnerability intelligence while safeguarding operational stability.
* **Application Security & CI/CD Gating:** deployed containerized Web Application Scanning sensors within internal network segments; integrated dynamic application security testing (DAST) into CI/CD pipelines and evaluated SAST/SCA tooling to identify software supply-chain exposures.
* **Stakeholder Alignment & Exposure Governance:** partnered directly with plant directors, substation supervisors, and infrastructure owners, delivering clear exposure risk briefings and staged passive-discovery demonstrations to prove zero operational impact, securing unanimous sign-off across critical operating units.

### Cybersecurity Systems Engineer / ACAS & Exposure Infrastructure Owner | RHEL Platform Owner
**USMC, Marine Corps Installations Command (MCICOM), KCITC Datacenter** | Kansas City, MO | Aug 2016 – Jul 2021
*Civilian Contractor for 22nd Century Technologies Inc. Platform owner for continuous exposure monitoring and vulnerability management systems across classified and unclassified DoD datacenter enclaves.*

* **Continuous Exposure Platform Ownership:** deployed, administered, and maintained the enterprise ACAS platform (Tenable.sc, Nessus, Nessus Network Monitor) and supporting Red Hat Enterprise Linux infrastructure across multi-tier datacenter enclaves; designed the comprehensive Vulnerability Management Strategy and Continuous Monitoring plan.
* **Telemetry Ingestion & SIEM Integration:** integrated ACAS vulnerability telemetry and host audit streams into Splunk Enterprise and syslog-ng; engineered custom dashboards, correlation queries, and exposure tracking reports for cybersecurity leadership and platform teams.
* **Automated Exposure Remediation & Baseline Enforcement:** developed Ansible automation at fleet scale to enforce DISA STIG baselines, remediate configuration exposures, and deploy rapid patch countermeasures across diverse VLANs and security enclaves.
* **Vulnerability Querying & RMF Compliance:** executed direct SQL and database-level querying against vulnerability repositories to track IAVM compliance, validate remediation evidence, and support the ISSM with POA&M maintenance under enclave ATO packages.
* **Network Discovery Automation:** automated monthly and ad-hoc asset discovery workflows utilizing nmap, Python, PowerShell, and Bash to identify rogue hosts and maintain 100% asset accounting across classified boundaries.

### Cybersecurity Analyst Sr / ACAS Engineer
**USMC, Marine Corps Enterprise Information Technology Services (MCEITS Program)** | Kansas City, MO | Apr 2015 – Aug 2016
*Civilian Contractor for SAIC.*

* **ACAS Infrastructure Administration:** administered enterprise ACAS infrastructure, managing scan policy configuration, scanner pool load balancing, and underlying RHEL operating system security.
* **Attack Surface Coverage & Asset Accounting:** designed scheduled and ad-hoc discovery scans in Tenable SecurityCenter, maintaining comprehensive asset lists and eliminating coverage gaps across static and dynamic server subnets.
* **Audit Response & Patch Maintenance:** supported DoD cybersecurity inspections by extracting authoritative vulnerability and compliance evidence; executed routine OS and application patching across all exposure assessment servers.

### Software Administrator & Application Engineer
**USMC, Marine Corps Enterprise Information Technology Services (MCEITS Program)** | Kansas City, MO | Jun 2014 – Apr 2015
*Civilian Contractor for CompQSoft.*

* **Infrastructure Telemetry & Monitoring:** administered enterprise infrastructure monitoring systems across datacenter enclaves, configuring performance thresholds, alert triggers, and automated notification channels.
* **Scripted Automation:** engineered PowerShell utilities to query system metrics, extract configuration baselines, and automate operational maintenance tasks.

### Earlier Engineering Experience

**Tier II Systems Analyst / Technical Escalation Lead**, ScriptPro, Mission, KS | 2011 – 2014
*Technical escalation lead and triage bridge between Tier 2 and Tier 3 engineering for automated robotics pharmacy systems across hospital networks. Configured Cisco ASA/PIX firewalls, 881 EZ-VPN routers, and switches, and performed packet-level troubleshooting with Wireshark to resolve network connectivity and security issues.*

**Production Support Analyst**, Cerner Corporation, Kansas City, MO | 2010 – 2011
*Production Level 2 support for clinical enterprise software. Executed direct SQL and CCL diagnostics against Cerner Millennium relational databases to identify data corruption, query transaction logs, and resolve complex application discrepancies.*

---

## Applied AI & Agent Security Engineering

### Auralith | Automated LLM Threat Modeling & Vulnerability Framework
*Creator & Lead Developer | Independent Open-Source R&D | Jan 2026 – Present | [GitHub](https://github.com/Ninponeer)*
* **Modular Exposure Evaluation:** architected a modular Python security evaluation framework integrating adapter layers (NVIDIA NIM, Nous Research, OpenAI/Anthropic endpoints) and an automated probe engine executing 48 probes across 14 categories mapped to MITRE ATLAS, NIST AI RMF, and OWASP Top 10 for LLMs.
* **Automated Risk Scoring & LLMPE:** integrated the 0din.ai Jailbreak Evaluation Framework (JEF) with standardized benchmark probes; authored the LLMPE specification establishing structured schemas for vulnerability scanning policies, exposure reporting, and threat scoring across Blast Radius, Retargetability, and Fidelity.

### Phoenix Protocol | Deterministic Agent Context & Attestation Architecture
*Systems Research | Independent | Jan 2025 – Present | [Research Portfolio](https://github.com/Ninponeer/feathercloak-consulting)*
* **Context Integrity & Exposure Prevention:** designed an auditable state-integrity architecture for autonomous agent systems using challenge-response mutual attestation to detect context manipulation and execution coercion prior to tool invocation.
* **Adversarial Attack Analysis:** evaluated multi-turn context drift, indirect prompt injection across tool interfaces, and fail-safe exception handling to prevent unauthorized exposure in autonomous agent workflows.

### Agentic Cloud Security Prototype (AWS)
*Lead Engineer | Independent Prototype | 2026*
* **Automated Cloud Posture Audit:** built an autonomous tool-calling inspection agent (Python, LangChain) auditing cloud infrastructure exposure (AWS IAM trust boundaries, S3 bucket policies, security groups) and enforcing strict least-privilege tool execution.
* **Deterministic Policy Testing:** engineered Moto-backed mock AWS environments and automated regression suites to validate exposure detection accuracy, tool schemas, and least-privilege boundaries offline.

---

## Education & Certifications

* **CompTIA SecurityX (CASP+, CompTIA Advanced Security Practitioner)** | Active 2016 – 2028
* **CompTIA Security+ & CompTIA Network+** | Active 2014 – 2028
  *Credential ID: `F0KPXJGKH1V1Y4K2`* | [Verify via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2) | [Verify via Credly](https://www.credly.com/users/rick-metz)
* **Google AI Professional Certificate** | Google / Coursera | [Verify Credential](https://coursera.org/share/276a54873faacd98c146428b9404548e)
* **Associate of Science in Computer Network Systems** | ITT Technical Institute | GPA: 4.0
  *Highest Academic Honors · National Technical Honor Society · Alpha Beta Kappa Society*

---

*Technical artifacts, architecture samples, and project repositories (Auralith, Phoenix Protocol, cloud infrastructure automation) available upon request.*
