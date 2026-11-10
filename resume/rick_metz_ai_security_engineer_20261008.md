# Rick Metz

**Senior AI Security Engineer | Applied AI Defense, Model & Agent Red-Teaming, Infrastructure & Firmware Security**
Pleasant Hill, MO | Remote (U.S. Citizen) | 816-209-4771 | ninponeer@gmail.com
[LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer) | [Credly](https://www.credly.com/users/rick-metz)

---

## Professional Summary

Security engineer with 15+ years defending mission-critical enterprise systems, DoD computing enclaves, and physical OT/ICS utility grids, operating at the intersection of infrastructure defense, application security, and applied AI security engineering. Combines deep vulnerability lifecycle management, hardware/firmware attack surface reduction, and cloud infrastructure defense with applied AI security practice: adversarial model red-teaming, automated evaluation harnesses, runtime agent boundary defense, and AI gateway governance.

Currently leads enterprise security readiness for production developer AI agents (Claude Code, 100+ users) through the Azure AI Foundry Gateway at US Anesthesia Partners (USAP), instrumenting client-side execution boundaries, tool permissions, Model Context Protocol (MCP) connections, and Microsoft Purview DSPM for AI with mandatory per-user attribution. Creator and lead developer of Auralith (v0.3), an open-source AI security evaluation and automated probe framework mapped to MITRE ATLAS, NIST AI RMF, and OWASP Top 10 for LLMs, integrating the 0din.ai Jailbreak Evaluation Framework (JEF) to benchmark multi-model blast radius, retargetability, and output fidelity under adversarial pressure. Backed by 7 years of classified DoD datacenter systems defense under DISA STIGs and 4+ years securing 50,000+ assets at PG&E. Holds CompTIA SecurityX (CASP+).

---

## Core Competencies

| Domain | Skills |
| --- | --- |
| AI Security Engineering & Red-Teaming | Adversarial testing of frontier LLMs and agentic systems, prompt injection defense (direct and indirect), jailbreak evaluation (JEF), context manipulation, model extraction defense, MITRE ATLAS & NIST AI RMF mapping, automated evaluation probes (Auralith v0.3) |
| Agentic Systems, MCP & Sandboxing | Autonomous tool-calling agent security, developer coding agent risk mitigation (Claude Code), Model Context Protocol (MCP) authentication and dynamic client registration governance, runtime execution sandboxing, deterministic agent state integrity (Phoenix Protocol), policy-driven tool refusal, least-privilege API boundaries |
| AI Gateways, Telemetry & Data Protection | AI Gateway security (Azure AI Foundry Gateway, Azure APIM, reverse proxies), prompt visibility, token-usage and quota governance, Microsoft Purview DSPM for AI (sensitivity labels, auto-labeling, DLP rules), per-user attribution, SIEM telemetry integration (Trellix Helix, Microsoft Sentinel pilot, Splunk) |
| Software, Firmware & Hardware Security | Threat modeling across software, APIs, and embedded IoT hardware; firmware/BMC vulnerability assessment; secure code reviews and remediations (Python, Go, Bash); DAST/SAST/SCA pipeline integration; input sanitization and memory safety |
| Cloud Security & Infrastructure Automation | AWS and Azure private-endpoint and zero-public-egress topologies (Azure Functions, Event Hubs, VNet integration, NSGs), Docker container isolation and containerized security sensors, reusable Python API toolkits and data pipelines (asyncio, REST APIs, pandas/Jupyter), Ansible automation at fleet scale, GitHub CI/CD security gating |
| OT/ICS & Critical Infrastructure Defense | Securing distributed hardware sensors, SCADA/ICS enclaves, air-gapped networks, continuous passive network monitoring (NDR / Nessus Network Monitor), non-disruptive vulnerability assessment across 50,000+ operational and embedded physical assets |
| Vulnerability Lifecycle & Governance | Root-cause flaw identification, CVSS/VPR/EPSS risk scoring, exploit maturity analysis, remediation campaigns (remediating ~1,000 vulnerabilities in 30 days to sustain zero findings past SLA), NIST 800-53, DoD RMF, DISA STIG / SRG, HITRUST CSF |

---

## Professional Experience

### Security Engineer / Tenable SME | Remediation Program Lead & AI Security Readiness
**Vaco (Contract Consultant), US Anesthesia Partners (USAP)** | Remote | Mar 2026 – Present
*Security engineering for a specialized healthcare organization: ~3,000 managed assets across a hybrid, multi-region footprint on a strictly Microsoft/Azure stack with Cisco network infrastructure.*

* **Enterprise AI & Agent Infrastructure Security:** lead enterprise security readiness for developer adoption of frontier coding agents (Claude Code, 100+ users) routed through the Azure AI Foundry Gateway. Engineered SIEM telemetry ingestion into Trellix Helix covering AI gateway traffic, Defender for Cloud AI threat signals, and client-side agent execution events: MCP server connections, dynamic client registration, tool permissions, and sandbox escapes.
* **Prompt Governance, DLP & Attribution:** own prompt visibility, token-usage and quota governance, and DSPM for AI protection. Partnered with engineering and compliance stakeholders to enforce mandatory per-user/service attribution on all AI gateway calls, prompt/response inspection, and data loss prevention (Microsoft Purview sensitivity labels, auto-labeling, and DLP rules) to prevent prompt injection and unauthorized medical data exfiltration.
* **Production Telemetry Pipeline (Argus):** authored a serverless Python Azure Function in ~6 days to close a SecOps visibility gap on WorkDay logs during a high-profile phishing campaign with active network probing. Configured VNet integration, Private Endpoints, NSGs, and secure outbound routing for zero public internet egress; now the organization's reference pattern for onboarding SaaS log sources requiring pull-and-normalize.
* **Detection & Vulnerability Program Leadership:** stabilized Trellix Helix and partnered with a second engineer to pilot Microsoft Sentinel. Designed the end-to-end vulnerability remediation program from scratch (campaign model, severity/SLA matrix, risk-acceptance process), driving a campaign against a breached Critical/High backlog that remediated ~1,000 vulnerabilities in ~30 days, sustaining no findings past SLA.
* **Automation Tooling & Code Reviews:** authored a reusable, documented Python Tenable API toolkit and Python/Jupyter data pipelines converting scanner exports into analysis-ready datasets. Conducted code-level reviews (Python, Go) with software engineering leads and established secure coding standards aligned with NIST 800-53 and HITRUST CSF.

### Cybersecurity Solutions Engineer / Tenable SME | Primary SME & VM Program Architect
**Pacific Gas & Electric** | Remote | Sep 2021 – Jan 2026
*Embedded security consultant via World Wide Technology, with MatchPoint and IS3 Solutions as delivery partners. Primary Tenable SME for a Fortune 500 utility: vulnerability management across on-premises datacenters, distributed facilities, multi-cloud (AWS, Azure), air-gapped networks, and OT/ICS, spanning 50,000+ assets.*

* **Physical Operations & Firmware/Hardware Defense:** architected non-disruptive vulnerability assessment and sensor deployment across sensitive industrial control systems (ICS/SCADA), substation gateways, and embedded field hardware, eliminating blind spots while preventing operational disruption across critical physical infrastructure.
* **Continuous Passive Network Monitoring (NNM):** deployed and maintained Nessus Network Monitor for continuous passive monitoring of critical assets, surfacing unmanaged devices, shadow IoT systems, and unauthorized cross-zone communications without active probing.
* **Cross-Boundary Automation & Data Diodes:** built hardened Python and Bash data transport pipelines moving security intelligence, Tenable plugins, and patches through DMZ data diodes into air-gapped networks, then exporting scan results back out for central aggregation, eliminating 8+ hours of weekly manual work.
* **Privileged Access Automation:** integrated BeyondTrust Password Safe with Tenable.sc via a Python service fetching automatically rotated credentials across Linux and Windows server fleets, strictly enforcing least-privilege access and eliminating scan failures from credential expiry.
* **Asset Discovery & CI/CD Security:** built an Infoblox REST API integration enumerating subnets to drive dynamic Tenable.sc asset tagging. Deployed containerized Web Application Scanning (WAS) sensors inside internal segments; integrated DAST into CI/CD build pipelines and evaluated SAST/SCA tooling for supply-chain risk.
* **Stakeholder Alignment:** partnered with plant directors and station supervisors to overcome monitoring resistance through staged demonstrations of zero-impact passive discovery, achieving unanimous sign-off with zero operational disruption.

### Cybersecurity Systems Engineer / ACAS & Tenable SME | RHEL Infrastructure Owner
**USMC, Marine Corps Installations Command (MCICOM), KCITC Datacenter** | Kansas City, MO | Aug 2016 – Jul 2021
*(Cybersecurity Systems Engineer 2016–2021 | Cybersecurity Analyst Sr 2015–2016 | Systems Administrator 2014–2015)*
*Civilian Contractor for 22nd Century Technologies, SAIC, and CompQSoft. Engineered and administered security platforms across classified and unclassified DoD enterprise computing environments under strict confidentiality constraints.*

* **Baseline Enforcement as Code:** authored Ansible playbooks to automate security control enforcement, STIG validation, and configuration remediation across large RHEL and Windows server fleets under DISA STIG and DoD RMF requirements.
* **Automated Auditing & Discovery:** built Python, Nmap, and PowerShell tooling to identify rogue hardware, unauthorized services, and configuration drift across segmented enclaves.
* **Platform Administration & ISSM Support:** owned deployment and maintenance of ACAS (Tenable.sc, Nessus, NNM), Splunk, Lansweeper, and Red Hat Satellite. Worked directly with the ISSM on IAVM compliance and POA&M maintenance for systems under enclave ATO packages.
* **Detection Engineering:** engineered log collection and security monitoring across DoD datacenter enclaves using Splunk; authored detection queries, correlation rules, and executive posture reports.

### Earlier Engineering Experience

**Tier II Systems Analyst / Technical Escalation Lead**, ScriptPro, Mission, KS | 2011 – 2014
*Technical escalation lead for automated robotic systems in healthcare networks. Configured Cisco ASA firewalls, switches, and IPsec VPNs; performed packet-level troubleshooting with Wireshark.*

**Production Support Analyst**, Cerner Corporation, Kansas City, MO | 2010 – 2011
*Application and database support for clinical systems using SQL diagnostics in Cerner Millennium environments.*

---

## Applied AI Security & Agent Engineering Projects

### Auralith | Automated LLM Threat Modeling & Vulnerability Framework
**Independent Open-Source R&D** | Creator & Lead Developer | Jan 2026 – Present | [GitHub](https://github.com/Ninponeer)

* **Automated AI Risk Assessment:** engineered a modular Python security evaluation framework applying traditional vulnerability management disciplines to LLMs, autonomous agents, and RAG backends: target discovery, scan policies, adapter execution, and risk scoring.
* **NIST AI RMF & MITRE ATLAS Mapping:** implemented an automated probe engine featuring 94 detection probes across 16 categories aligned with NIST AI RMF, MITRE ATLAS, and OWASP Top 10 for LLMs / Agentic AI to measure model boundary resilience.
* **Jailbreak Benchmark & Blast Radius Scoring:** integrated the 0din.ai Jailbreak Evaluation Framework (JEF) to benchmark model resistance against adversarial attacks, computing multi-model Blast Radius (BV/BM), Retargetability (RT), and Fidelity (FD) across frontier endpoints.
* **Multi-Model Adapters:** built integration adapters across Anthropic, OpenAI, NVIDIA NIM, and open-weights runtimes, enabling standardized multi-model vulnerability scans and executive risk reporting.

### Phoenix Protocol | Deterministic Agent Context & Attestation Architecture
**Systems Research** | Independent | Jan 2025 – Present | [Research Portfolio](https://github.com/Ninponeer/feathercloak-consulting)

* **State Integrity Architecture:** designed an auditable state-integrity architecture for autonomous agents using challenge-response mutual attestation to detect runtime context manipulation and execution coercion prior to tool use.
* **Adversarial Context Defense:** analyzed attack vectors involving multi-turn context drift, indirect prompt injection across agentic tools, and safe fallback handling for agentic workflows.

### Agentic Cloud Security Prototype (AWS)
**Lead Engineer** | Independent Prototype | 2026

* **Autonomous Tool-Calling Security:** built an autonomous tool-calling inspection agent (Python, LangChain) auditing cloud posture (AWS IAM boundaries, S3 bucket policies, security groups), validating least-privilege tool execution and refusal behavior under adversarial inputs.
* **Deterministic Boundary Testing:** built Moto-backed mock AWS environments and automated regression suites to evaluate agent decision boundaries, schema validation, and safe exception-handling fallbacks.

---

## Education & Certifications

* **CompTIA SecurityX (CASP+, Advanced Security Practitioner)** | CompTIA • Active 2016 – 2028
* **CompTIA Security+ • CompTIA Network+** | CompTIA • Active 2014 – 2028
  *Credential ID: `F0KPXJGKH1V1Y4K2`* | [Verify via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2) | [Verify via Credly](https://www.credly.com/users/rick-metz)
* **Google AI Professional Certificate** | Google • Coursera | [Verify Certificate](https://coursera.org/share/276a54873faacd98c146428b9404548e)
* **Associate of Science in Computer Network Systems** | ITT Technical Institute • GPA: 4.0
  *Highest Academic Honors • National Technical Honor Society • Alpha Beta Kappa Society*

---

*Technical artifacts, architecture samples, and project repositories (Auralith, Phoenix Protocol, cloud infrastructure automation) available upon request.*
