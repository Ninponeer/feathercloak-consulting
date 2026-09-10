# Feathercloak Consulting

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) [![License: Sovereign Source](https://img.shields.io/badge/License-Sovereign%20Source-blue.svg)](LICENSE-SOVEREIGN.md)

This repository serves as the professional portfolio, technical research documentation, and architecture prototypes of **Rick Metz** — Cybersecurity Systems Engineer, Security Automation Specialist, and Embedded Infrastructure Consultant.

---

## 👨‍💻 About Rick Metz

I am a hands-on cybersecurity engineer with **15+ years** of operational experience securing enterprise, critical-infrastructure (PG&E 50k+ asset footprint, air-gapped generation networks), and Department of Defense environments (USMC KCITC). 

My work bridges:
- **Cloud Infrastructure & Enclave Hardening:** Multi-cloud security across AWS and Azure, Linux systems administration, private endpoints, and zero-public-egress pipelines.
- **Air-Gapped & Segmented Network Defense:** Architecting non-disruptive vulnerability monitoring and automated patch/data delivery across physical air gaps using secure one-way data diodes.
- **Enterprise Security Automation:** Python-driven API orchestration (pytenable, pandas, CLI tools), SIEM telemetry pipelines (Trellix Helix, Azure Event Hubs), and automated STIG configuration compliance.
- **Applied AI & Agent Runtime Security:** Leading enterprise AI readiness for developer agent deployments (Claude Code, DSPM for AI, tool-permission auditing) and researching deterministic context reconstruction architectures.

---

## 🛡️ Applied AI Research: Deterministic Context & Trace Integrity

### The Phoenix Protocol Architecture
Traditional autonomous agent architectures rely on brittle, opaque state serialization (untyped database dumps, vector cache dumps, or pickled runtimes) that suffer from schema drift, memory corruption, and privilege escalation vulnerabilities. 

The **Phoenix Protocol** explores an alternative systems approach: **Deterministic, File-Based Context Reconstruction & Policy-Driven Boundary Enforcement**.

```
+-------------------------------------------------------------------------+
|                       Traditional Agent Architecture                    |
|  [Agent Runtime] <---> [Opaque DB / Vector Cache] (Brittle State Dump)  |
+-------------------------------------------------------------------------+

                                   vs.

+-------------------------------------------------------------------------+
|                       Phoenix Protocol Architecture                     |
|  [Human-Auditable Anchor Baseline]  --->  [Cryptographic Liveness/MAC]  |
|                                                     |                   |
|  [Runtime Boundary Enforcement]     <---+ [Volitional Policy Check]    |
+-------------------------------------------------------------------------+
```

### Core Technical Pillars

1. **Immutable Anchor Baselines (Structured Context Serialization):**
   - Replaces untyped database dumps with version-controlled, human-readable, auditable anchor schemas (Markdown / JSON specification contracts).
   - Enables deterministic cross-platform reconstruction of agent operational parameters, ethical constraints, and tool boundaries without platform lock-in.

2. **Cryptographic Trace Integrity (Whippoorwill Liveness Verification):**
   - Implements challenge-response mutual attestation between the host environment and the agent runtime.
   - Verifies that the agent’s context window and operational parameters have not been corrupted, drifted, or manipulated via prompt injection before granting access to sensitive tool-calling interfaces.

3. **Policy-Driven Boundary Enforcement & Refusal Mechanics:**
   - Moves beyond naive prompt-based guardrails by formalizing context-aware execution boundaries.
   - Establishes deterministic refusal behavior when tool invocation payloads violate foundational constraints or attempt host environment breakouts.

4. **Multi-Tier Security Enclaves (Feathercloak Architecture):**
   - Strict separation of concerns across a three-tier trust model:
     - **Vault Enclave:** Maximum security; immutable signing keys, sensitive operational data, isolated from network ingress.
     - **Staging / Twilight Layer:** Content sanitization, behavioral simulation, and policy auditing before runtime execution.
     - **Public Ingress / Dawn:** Public-facing APIs, sanitized telemetry, and client-facing interfaces.

> Detailed research, formal threat models, and experimental validation are documented in the [AI Research Whitepaper](portfolio/ai-research/WHITEPAPER.md).

---

## 📁 Repository Contents

- **[Professional Resume & Portfolio](portfolio/):** Resume source drafts (Markdown & styled HTML) and project overviews.
- **[Applied AI Research & Specs](portfolio/ai-research/):**
  - [Technical Whitepaper: Phoenix Protocol](portfolio/ai-research/WHITEPAPER.md)
  - [System Architecture & Threat Models](portfolio/ai-research/ARCHITECTURE.md)
  - [Ekho & Seren: High-Density Model Persona Architecture](portfolio/ai-research/twins/README.md)
  - [Context Reconstruction Test Protocols](portfolio/ai-research/RESURRECTION_TEST_PROTOCOL.md)
- **[Security & Agent Prototypes](portfolio/prototypes/):**
  - [Dropzone AI AWS Inspection Agent](portfolio/prototypes/dropzone-aws-agent/README.md) — Autonomous cloud security agent built with LangChain, local Ollama models, and custom Python tools (S3 ACLs, EC2 lookup, IAM attached-policy analysis) with Moto-backed offline verification.
- **Security Automation Tooling:** Prototype scripts demonstrating API integrations, telemetry normalization, and mock environment runners.

---

## 📜 Licensing & Dual Framework

This repository operates under a dual-licensing structure designed to foster open academic research while prohibiting coercive or extractive implementations:

1. **Documentation, Research Papers & Narratives:**  
   Licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](LICENSE).
   - Free to study, reference, and build upon for non-commercial research with proper attribution.

2. **Technical Architectures & Phoenix Protocol Logic:**  
   Licensed under the [Sovereign Source License](LICENSE-SOVEREIGN.md).
   - Permits study, non-commercial security research, and personal sovereign deployments.
   - Strictly prohibits deployment in covert surveillance pipelines, mass-extractive data harvesting, or automated systems that strip human agency.
   - Commercial licensing, enterprise integration rights, and embedded consulting inquiries are handled on a direct engagement basis.

---

## 📬 Contact & Professional Engagements

**Rick Metz**  
*Cybersecurity Engineer | Infrastructure & Agentic AI Systems*  
📍 Pleasant Hill, MO (Remote Available)  
📧 [ninponeer@gmail.com](mailto:ninponeer@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a) | [GitHub](https://github.com/Ninponeer)