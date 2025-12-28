# Rick Metz
Cybersecurity Engineer | Automation & Vulnerability Management Specialist  
Pleasant Hill, MO | 816–209–4771 | ninponeer​@​gmail​.​com  
[LinkedIn](https://www.linkedin.com/in/rick-metz-29228421a)

---

## Professional Summary
Strategic Cybersecurity Engineer with 15+ years of experience spanning IT operations, systems engineering, and security program development. Specialized in solving the most challenging stability and coverage problems in Vulnerability & Exposure Management through Tenable platform design, API integrations, and automation pipelines built on Python and infrastructure-as-code principles. Proven track record designing full credentialed scan implementations and architecting enterprise scan strategies that ensure stable operations across network, application, and database stacks. Trusted embedded consultant delivering strategic solutions for Fortune 500 clients and federal datacenter environments, including complex air-gapped networks.

---

## Certifications
- **CompTIA SecurityX** (2016–2028)  
- **CompTIA Security+** (2014–2028)  
- **CompTIA Network+** (2014–2028)  

🔗 [Verify Credentials via CompTIA](https://www.certmetrics.com/comptia/public/transcript.aspx?transcript=F0KPXJGKH1V1Y4K2)

---

## Core Competencies

**Vulnerability Management**  
Tenable.sc, Nessus, Nessus Agents, Nessus Network Monitor (NNM), Tenable.io, ACAS, Credentialed Scanning, Passive Monitoring, ICS/OT Scanning

**Security Configuration & Compliance**  
STIG/SRG Hardening, SCAP, NIST RMF, CIS Benchmarks, IAVM Management, POA&M Tracking, ATO Package Support

**Scripting, Automation & Integration**  
Python, Bash, PowerShell, REST API Development, Scheduled Task Automation, Data Pipeline Orchestration

**OS Administration & Configuration Management**  
Red Hat Enterprise Linux, Red Hat Satellite, Ansible, AWX, Windows Server, Privilege Elevation (sudo, WinRM, Cisco 'enable')

**SIEM, EDR & Log Aggregation**  
Splunk Enterprise, Splunk Enterprise Security, Syslog-ng, rsyslog, SC4S

**Platform Integrations**  
BeyondTrust PAM, Infoblox IPAM, Dell EMC Data Domain, Air-Gapped Architectures, Credential Rotation Automation

**Network Administration & Discovery**  
Infoblox, Lansweeper, Wireshark, nmap, Cisco ASA/PIX, EZ-VPN Routers

**Virtualization**  
VMware vSphere, vCenter, vRealize

**Tools & Collaboration**  
Git, VS Code, Jira, ServiceNow, Remedy, Microsoft Office Suite, Visio  

---

## Professional Experience

### Cybersecurity Solutions Engineer / Tenable SME  
**Pacific Gas & Electric (Embedded Consultant via WWT & Asterya/IS3)** | Remote | Sep 2021 – Present

Serving as the organization's Primary Tenable Subject Matter Expert (SME), I designed and led the deployment of enterprise-scale Tenable platforms across a complex, highly distributed network. Engineered the Vulnerability Management program to achieve continuous monitoring and reduce organizational risk, with particular focus on complex, sensitive, and air-gapped network segments.

- Partnered with stakeholders to assess Tenable deployment, identify visibility gaps, and design strategic enhancements
- Delivered optimized vulnerability management solutions that expanded coverage, reduced risk exposure, and improved remediation efficiency
- Acted as trusted advisor, strengthening client relationships and supporting long-term business development by aligning technical solutions with organizational goals
- Enabled adoption of enhanced detection and reporting capabilities, positioning the client for scalable growth in their security program

**Tenable Platform Design & Optimization**  
- Architected comprehensive enterprise scan strategy with staggered logic ensuring application, database, and core network stacks maintained stability during high-volume assessments
- Implemented full credentialed scanning across all supported operating systems with secure privilege elevation mechanisms (`sudo`, `WinRM`, `Cisco 'enable'`) maximizing scan depth and accuracy
- Eliminated network blind spots by deploying Nessus Network Monitor (NNM) for continuous, non-intrusive passive vulnerability monitoring of critical assets
- Developed custom, non-disruptive scan policies for sensitive ICS/OT environments, providing active vulnerability data without impacting system stability

**Signature Projects & Integrations**

*Air-Gapped Network Automation*  
Automated the full lifecycle of vulnerability data and patch management for Tenable.sc instances in highly secure, air-gapped environments where direct internet connectivity is prohibited.
- Developed Python and Bash scripts to securely pull Tenable plugin sets, SC feeds, and software patches from internet-connected repositories
- Engineered secure transport leveraging Dell EMC Data Domain with one-way replication to transfer updates into isolated network segments
- Automated import/export of scan results through secure channels for aggregation in central consoles
- **Impact**: Eliminated 8+ hours of weekly manual work, reduced human error, and ensured mission-critical isolated systems received timely vulnerability intelligence

*Infoblox & Tenable Integration for Dynamic Asset Discovery*  
Established a single source of truth for network ranges by dynamically creating and updating Tenable.sc asset lists from authoritative Infoblox IPAM data.
- Built Python service querying Infoblox REST API for comprehensive subnet and network container data
- Implemented intelligent grouping by business unit, geographic location, and custom Infoblox attributes
- Automated Tenable.sc "Combination" asset list creation/updates via REST API for discovery and vulnerability scans
- **Impact**: Closed significant scan coverage gaps, eliminated network blind spots, and removed error-prone static IP list maintenance

*BeyondTrust PAM Integration for Credential Rotation*  
Hardened vulnerability scanning security by automating privileged credential management between BeyondTrust Password Safe and Tenable.sc.
- Integrated Tenable.sc with BeyondTrust PAM for secure credential vaulting
- Developed Python automation to fetch rotated passwords for scanning accounts (Windows Domain Admin, Linux root)
- Dynamically updated SSH and SMB credentials in Tenable.sc to prevent scan failures from stale passwords
- **Impact**: Eliminated static, long-lived scanning passwords; enforced strict rotation policies; ensured reliable authenticated scanning

*Operational Scripting*  
- Developed custom integration scripts to automate system maintenance, health checks, and data pipeline integrity checks
- Improved platform stability and reduced operational overhead through proactive automation  

---

### USMC – KCITC Datacenter | Kansas City, MO | Jun 2014 – Jul 2021
Progressed through three distinct roles supporting Marine Corps Installations Command (MCICOM) and Marine Corps Enterprise IT Services (MCEITS) programs, demonstrating continuous skill development and increasing responsibility across mission-critical datacenter environments.

---

#### Cybersecurity Systems Engineer / ACAS & Tenable SME  
**Civilian Contractor for 22nd Century Technologies Inc.** | Aug 2016 – Jul 2021

Promoted to lead cybersecurity engineering role responsible for deployment, maintenance, and daily administration of all cybersecurity systems and Red Hat Enterprise Linux infrastructure. Served as primary POC for STIG/SRG compliance and vendor hardening guide adherence. Primary escalation point for complex system configuration issues and vulnerabilities not addressable via routine patching. Collaborated closely with ISSM on IAVM compliance and POA&M maintenance across enclave ATO packages.

**Key Responsibilities**  
- Deployed, configured, and maintained ACAS (Tenable.sc, Nessus, NNM), Splunk, Lansweeper, Syslog-ng, and rsyslog
- Deployed and maintained Red Hat Satellite and RHEL-based application servers
- Designed and implemented comprehensive Vulnerability Management strategy and Continuous Monitoring plan
- Created and managed static and dynamic asset lists within Tenable.sc ensuring full visibility for vulnerability and SCAP compliance scans
- Utilized infrastructure monitoring tools to automate security-related event alerts and log auditing
- Coordinated with internal and external resources to mitigate/remediate vulnerabilities with minimal production impact

**Automation & Engineering Contributions**  
- Facilitated partial automation of monthly and ad-hoc network discovery scans using nmap, PowerShell, Bash, and Python
- Developed Ansible content to automate common system tasks, deploy STIG baseline configurations, and enforce security controls across multiple VLANs and enclaves
- Built custom dashboards, components, and reports in Tenable.sc and Splunk Enterprise for internal and external stakeholders
- Conducted continuous research into emerging security threats and vulnerabilities

---

#### Cybersecurity Analyst Sr / ACAS Engineer  
**Civilian Contractor for SAIC** | Apr 2015 – Aug 2016

Advanced to senior analyst role with expanded ownership of ACAS platform and underlying RHEL infrastructure. Took on scan policy design responsibilities and compliance audit response duties.

**Key Responsibilities**  
- Responsible for deployment, maintenance, and daily administration of all ACAS systems and underlying Red Hat Enterprise Linux operating systems
- Designed and maintained comprehensive scans and scan policies within Tenable Security Center to maintain high confidence in organizational security posture
- Performed scheduled and ad-hoc network discovery scans ensuring all assets were accounted for and scanned regularly
- Created and managed asset lists within Tenable Security Center for full network visibility
- Responded to cybersecurity and compliance audits (both manual and automated) to maintain strong security posture
- Stayed appraised of emerging security vulnerabilities; coordinated with external resources to provide mitigation with minimal impact
- Responsible for OS and application patching on all ACAS systems

---

#### Software Administrator & Application Engineer  
**Civilian Contractor for CompQSoft** | Jun 2014 – Apr 2015

Entry point into federal datacenter environment, focused on infrastructure monitoring tools and operational efficiency improvements. Developed foundational scripting skills that would become central to later cybersecurity automation work.

**Key Responsibilities**  
- Administered and maintained infrastructure monitoring tools across various enclaves
- Implemented new monitoring solutions, configuring alerts, monitors, and performance metrics
- Monitored system metrics and developed reports for system analysis
- Prepared and installed solutions by determining customer requirements, designing system specifications, and establishing monitoring standards
- Improved operational efficiency by collaborating with multiple teams to develop monitors and alerts tracking health and stability of information systems
- Developed and utilized PowerShell scripts to retrieve information from systems and automate common tasks
- Provided assessments to management on risks and benefits of proposed solutions
- Communicated progress on outage resolution to management and application owners

**Foundation Skills Developed**  
- PowerShell scripting for automation and data retrieval
- Infrastructure monitoring implementation and configuration
- Cross-team collaboration in datacenter environments
- Technical assessment and documentation practices  

---

### Earlier Career

**Tier II Customer Support / Application Systems Analyst I** – ScriptPro, Mission, KS (2011–2014)  
- Provided Tier 2 support for robotics pharmacy systems (Windows NT/XP/7, Server 2003/2008)
- Installed and configured Cisco ASA/PIX firewalls, 881 EZ-VPN routers, and network switches
- Developed interface data extraction/modification rules; wrote SQL queries for database integrity and maintenance
- Created technical documentation including network wiring diagrams and interface configurations (Visio)

**Production Support Analyst** – Cerner, Kansas City, MO (2010–2011)  
- Provided Level 2 support for Cerner healthcare software (PharmNET, PathNET, XRPrint Services)
- Used CCL (SQL) for database troubleshooting and data operations within Cerner Millennium environments
- Created client-specific documentation and detailed walkthrough guides for complex procedures

---

## Education
**Associates in Computer Network Systems** – ITT Technical Institute (2008–2010, GPA 4.0)  
- Highest Academic Honors, National Technical Honor Society, Alpha Beta Kappa Society

---

## References
Available upon request
