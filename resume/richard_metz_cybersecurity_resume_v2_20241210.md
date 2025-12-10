# Rick Metz
Cybersecurity Systems Engineer | Security Automation & Platform Engineering  
Pleasant Hill, MO | 816‑209‑4771 | ninponeer@gmail.com  
[LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a)

---

## Professional Summary
Cybersecurity Systems Engineer with 15+ years of experience architecting and deploying enterprise-scale security infrastructure across hybrid environments spanning on-premises datacenters, distributed facilities, air-gapped networks, and multi-cloud platforms (AWS, Azure). Deep expertise in vulnerability management platforms (Tenable.sc/ACAS), multi-cloud security architecture, and security automation through full-stack Python development and REST API integration. Proven track record designing and implementing scalable security solutions that reduce risk while enabling business operations across diverse infrastructure topologies. Combines technical depth with strong communication skills, serving as embedded consultant and subject matter expert across diverse stakeholder groups.

---

## Core Competencies

**Infrastructure & Cloud Security**  
Multi-Cloud Security Architecture (AWS, Azure), Vulnerability Management (Tenable.sc/ACAS, Tenable Vulnerability Management [SaaS], Tenable Web Application Scanners), Container Security (Docker), Network Security Monitoring (NNM), Credentialed Scanning, Application Security Scanning (SAST/DAST/IAST), STIG/CIS Hardening, SIEM (Splunk)

**Identity & Access Management**  
Privileged Access Management (PAM), Automated Credential Rotation, Role-Based Access Control (RBAC), Secret Management, Secure Privilege Elevation

**Security Automation & Integration**  
`pytenable`, `infoblox-client`, `paramiko`, `pywinrm`, `ansible` (Python API), `splunk-sdk`, REST API Development, Process Automation, Infrastructure-as-Code (Ansible)

**Software Engineering & Architecture**  
Modular System Design, API Client Development, Full-Stack Python Development, Data Modeling & Serialization (JSON/YAML), CLI Tool Development, Automated Testing & Validation, Performance Optimization

**Languages & Tools**  
**Python** (Expert), **PowerShell**, **Bash**, Git, Docker, Ansible, Pytest, VMware, Nmap, Wireshark

---

## Professional Experience

### Cybersecurity Solutions Engineer / Tenable SME
**Pacific Gas & Electric (Embedded Consultant)** | Remote | Sep 2021 – Present

Serving as primary Tenable Subject Matter Expert, architecting and leading deployment of enterprise-scale vulnerability management solutions across complex, geographically distributed infrastructure.

**Hybrid Infrastructure Security & Platform Engineering**
- Architected vulnerability assessment strategy for hybrid infrastructure spanning on-premises datacenters, geographically distributed facilities, air-gapped networks, and multi-cloud environments (AWS, Azure) in collaboration with cloud engineering teams
- Engineered comprehensive enterprise scan strategy with staggered logic ensuring application, database, and network stack stability during high-volume assessments across complex, segmented state-wide networks and isolated network segments
- Implemented full credentialed scanning across all supported operating systems with secure privilege elevation mechanisms (`sudo`, `WinRM`, `Cisco 'enable'`), achieving authenticated vulnerability assessment at scale across both cloud and on-premises infrastructure
- Deployed containerized Tenable Web Application Scanner sensors using Docker for scalable application security testing across distributed infrastructure, replacing legacy WhiteHat Sentinel and expanding coverage to modern SAST/DAST/IAST domains
- Deployed Nessus Network Monitor (NNM) for continuous passive vulnerability monitoring across hybrid networks, eliminating blind spots in both cloud and on-premises environments and providing real-time threat visibility
- Developed custom, non-disruptive scan policies for sensitive ICS/OT environments and air-gapped network segments, balancing security requirements with operational stability

**Security Automation & Integration Projects**

*Air-Gapped Network Automation*
- Automated full lifecycle of vulnerability data and patch management for Tenable.sc instances in air-gapped environments using Python and Bash scripting
- Engineered secure transport mechanism leveraging Dell EMC Data Domain with one-way replication for isolated network segments
- **Impact:** Eliminated 8+ hours of weekly manual work, reduced human error, ensured timely vulnerability intelligence delivery to critical infrastructure

*Infoblox IPAM & Tenable Integration*
- Built Python service integrating Tenable.sc with Infoblox IPAM via REST APIs for dynamic asset discovery and inventory management
- Implemented intelligent asset grouping by business unit, geographic location, and custom attributes for targeted vulnerability assessments
- Automated creation and updates of Tenable.sc asset lists for discovery and vulnerability scans
- **Impact:** Closed significant scan coverage gaps, eliminated static IP list maintenance, improved asset visibility across enterprise

*BeyondTrust PAM Integration & Secret Management*
- Designed and implemented automated credential rotation system integrating Tenable.sc with BeyondTrust Password Safe
- Developed Python automation to fetch rotated passwords and dynamically update scan credentials with role-based access controls
- Implemented secret management controls limiting privileged credential exposure to authorized operations and engineering personnel only
- **Impact:** Eliminated static scanning passwords, enforced strict rotation policies, ensured reliable authenticated scanning while maintaining least-privilege access principles

---

### USMC – KCITC Datacenter | Kansas City, MO | Jun 2014 – Jul 2021

**Cybersecurity Systems Engineer / ACAS & Tenable SME** (Aug 2016 – Jul 2021)
- Led the deployment, maintenance, and administration of all cybersecurity systems, including ACAS (Tenable.sc, Nessus, NNM) and Splunk, for mission-critical datacenter environments supporting Marine Corps operations
- Architected and maintained vulnerability management infrastructure for classified and unclassified networks, ensuring compliance with DoD security requirements
- Developed Ansible content to automate STIG baseline configurations and security control enforcement across diverse operating systems
- Facilitated partial automation of network discovery scans using nmap, PowerShell, and Python, improving asset inventory accuracy

**Cybersecurity Analyst Sr / ACAS Engineer** (Apr 2015 – Aug 2016)
- Owned the ACAS platform and underlying RHEL infrastructure, designing and maintaining comprehensive vulnerability and compliance scan policies in Tenable Security Center
- Collaborated with system administrators and application owners to remediate critical vulnerabilities and maintain security posture
- Generated executive-level reports and metrics on vulnerability trends, remediation progress, and risk reduction

**Software Administrator & Application Engineer** (Jun 2014 – Apr 2015)
- Developed foundational automation skills by creating PowerShell scripts to retrieve system information and automate common administrative tasks, improving operational efficiency
- Supported enterprise application deployments and troubleshooting in Windows Server environments

---

## Technical Projects & Continuous Learning

### Lead Architect & Developer | Personal R&D: Procedural Generation Game Engine | 2025 – Present
*Demonstrating advanced Python development, systems architecture, and technical adaptability through self-directed learning*

Architected and developed a comprehensive, multi-engine procedural generation platform for a fantasy RPG, showcasing ability to design complex systems from the ground up and rapidly acquire new technical skills outside primary domain.

**Key Technical Achievements:**
- **Modular System Architecture:** Designed multi-threaded world generation engine following a "Six Days of Creation" pipeline (Foundation → Climate → Hydrology → Biomes → Life → Civilization), demonstrating systems thinking and modular design principles
- **Performance Optimization:** Implemented GPU-accelerated framework using CuPy with automatic CPU fallback (NumPy), achieving 5-10x performance increase—directly applicable to security data processing at scale
- **API Integration & Orchestration:** Architected unified asset generation pipeline integrating multiple AI/ML APIs (Google Gemini, PixelLabs) with robust client factory, rate limiting, error handling, and dynamic routing
- **CLI Tool Development:** Created comprehensive command-line interface using `argparse` for all pipeline operations, mirroring professional security tool development patterns
- **Data Validation & Quality:** Engineered validation gates between pipeline stages to enforce data integrity and target specifications—same discipline applied to security automation

**Relevance to Security Engineering:**
- Advanced Python development skills directly transferable to security automation and tooling
- Experience with API integration, error handling, and rate limiting applicable to security platform integrations
- Performance optimization mindset valuable for processing large-scale vulnerability and security data
- Demonstrates self-directed learning, technical curiosity, and ability to step outside comfort zone to deliver results

---

## Education & Certifications

**Associates in Computer Network Systems** – ITT Technical Institute (GPA 4.0)  
*Highest Academic Honors, National Technical Honor Society, Alpha Beta Kappa Society*

**CompTIA SecurityX** (2016–2028)  
**CompTIA Security+** (2014–2028)  
**CompTIA Network+** (2014–2028)  
*Credential ID: F0KPXJGKH1V1Y4K2*

**Professional Development:**
- AWS Architecture & Design (Video Course Series)
- Continuous learning in cloud security, container security, and modern DevSecOps practices

---

## Key Strengths

**Technical Depth:** Expert-level Python development, REST API integration, and security automation with proven ability to architect complex, scalable solutions

**Domain Expertise:** 10+ years as Tenable/ACAS subject matter expert with deep understanding of vulnerability management lifecycle, credentialed scanning, and enterprise security operations

**Communication & Collaboration:** Proven ability to translate complex technical concepts for diverse audiences, from engineers to executives, while serving as embedded consultant

**Problem-Solving:** Track record of identifying operational inefficiencies and developing automated solutions that reduce manual effort, improve accuracy, and scale security operations

**Adaptability:** Demonstrated ability to rapidly acquire new skills and technologies, stepping outside primary domain to deliver innovative solutions

---

## References
Available upon request
