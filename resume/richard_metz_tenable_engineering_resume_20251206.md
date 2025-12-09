# Rick Metz
Software Engineer | Automation & Systems Architecture  
Pleasant Hill, MO | 816‑209‑4771 | ninponeer@gmail.com  
[LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a)

---

## Professional Summary
A highly creative and disciplined Software Engineer with over 15 years of experience in IT and a deep passion for building robust, modular, and scalable systems. Proven expertise in full-stack Python development, REST API integration, and process automation. Adept at designing and implementing complex, data-driven pipelines from the ground up, with a strong focus on code quality, comprehensive documentation, and performance optimization. Eager to apply a background in security-conscious environments and a forward-thinking approach to engineering to contribute to Tenable's mission of reducing cyber risk.

---

## Core Competencies

**Software Engineering & Architecture**  
Modular System Design, API Client Development (REST), Full-Stack Python Development, Data Modeling & Serialization (JSON/YAML), Dependency Management, Test-Driven Development (TDD), Performance Benchmarking & Optimization, GPU Acceleration (CuPy)

**Automation & DevOps**  
CI/CD Pipeline Concepts, Process Automation, Infrastructure-as-Code (Ansible), CLI Tool Development, Automated Testing & Validation, Configuration Management, Secure Credential Management, Log Aggregation & Analysis

**Languages & Tools**  
**Python** (Expert), **PowerShell**, **Bash**, Git, Docker, Ansible, Pytest, VMware, Nmap, Wireshark

**Key Python Libraries**  
`google-genai`, `Pillow (PIL)`, `librosa`, `NumPy`, `SciPy`, `CuPy`, `requests`, `argparse`

**Vulnerability & Security Concepts**  
Vulnerability Management (Tenable.sc/ACAS), Credentialed Scanning, Passive Monitoring (NNM), STIG/CIS Hardening, SIEM (Splunk), Privileged Access Management (PAM)

---

## Technical Projects

### Lead Architect & Developer | Personal R&D: Procedural Generation Game Engine | 2025 – Present
Architected and developed a comprehensive, multi-engine procedural generation platform for a fantasy RPG as a personal R&D project, demonstrating end-to-end software design and engineering best practices.

**Procedural World Generation Engine**
- Designed and built a modular, multi-threaded world generation engine in Python, following a "Six Days of Creation" pipeline (Foundation → Climate → Hydrology → Biomes → Life → Civilization).
- Implemented a GPU-accelerated framework using CuPy for noise generation and data processing, with automatic CPU fallback (NumPy) for broader compatibility, achieving a 5-10x performance increase.
- Engineered validation gates between creation stages to enforce data integrity and target specifications (e.g., land coverage, elevation distribution), ensuring stable and predictable outputs.

**Hybrid AI Asset Generation Pipeline**
- Architected a unified asset generation pipeline integrating multiple AI/ML APIs (Google Gemini, PixelLabs) to create game-ready visual assets.
- Developed a robust API client factory for managing different providers, complete with rate limiting, error handling, and dynamic routing based on asset requirements (e.g., resolution, type).
- Built a complete post-processing and calibration toolkit using Pillow (PIL) for standardizing AI-generated images, including chroma key removal, height enforcement based on manifest data, and canvas centering.
- Created a comprehensive CLI (`argparse`) for all pipeline operations, including single asset generation, batch processing, model comparison, and asset registry management.

**Deterministic Scene Composition Engine**
- Designed a deterministic scene composition service to bridge the Python-based generation engines with the Godot game engine, ensuring multiplayer synchronization through hash-based scene resolution.
- Created a manifest-driven architecture to define scene descriptors, asset requirements, and export profiles for automated Godot project assembly.

**Procedural Audio & Music Engine**
- Developed a procedural music generation system using `librosa` for advanced audio analysis of reference compositions (WAV/MIDI).
- Implemented a pattern extraction framework to analyze tempo, key, mood, and spectral features, enabling the generation of context-aware, biome-specific soundscapes.

---

## Professional Experience

### Cybersecurity Solutions Engineer / Tenable SME
**Pacific Gas & Electric (Embedded Consultant)** | Remote | Sep 2021 – Present
- Served as the primary Tenable Subject Matter Expert, architecting and leading the deployment of enterprise-scale vulnerability management solutions across a complex, distributed network.
- Engineered a comprehensive enterprise scan strategy with staggered logic to ensure stability of application, database, and network stacks during high-volume assessments.
- Automated the full lifecycle of vulnerability data and patch management for Tenable.sc instances in air-gapped environments using Python and Bash, eliminating 8+ hours of weekly manual work.
- Built a Python service to integrate Tenable.sc with Infoblox IPAM via REST APIs, creating dynamic asset lists that closed significant scan coverage gaps and eliminated static IP list maintenance.

### USMC – KCITC Datacenter | Kansas City, MO | Jun 2014 – Jul 2021

**Cybersecurity Systems Engineer / ACAS & Tenable SME** (Aug 2016 – Jul 2021)
- Led the deployment, maintenance, and administration of all cybersecurity systems, including ACAS (Tenable.sc, Nessus, NNM) and Splunk, for mission-critical datacenter environments.
- Developed Ansible content to automate STIG baseline configurations and security control enforcement.
- Facilitated partial automation of network discovery scans using **nmap**, **PowerShell**, and **Python**.

**Cybersecurity Analyst Sr / ACAS Engineer** (Apr 2015 – Aug 2016)
- Owned the ACAS platform and underlying RHEL infrastructure, designing and maintaining comprehensive vulnerability and compliance scan policies in Tenable Security Center.

**Software Administrator & Application Engineer** (Jun 2014 – Apr 2015)
- Developed foundational automation skills by creating **PowerShell scripts** to retrieve system information and automate common administrative tasks, improving operational efficiency.

---

## Education & Certifications

**Associates in Computer Network Systems** – ITT Technical Institute (GPA 4.0)
- *Highest Academic Honors, National Technical Honor Society, Alpha Beta Kappa Society*

**CompTIA SecurityX** (2016–2028)  
**CompTIA Security+** (2014–2028)  
**CompTIA Network+** (2014–2028)  
*Credential ID: F0KPXJGKH1V1Y4K2*

---

## References
Available upon request