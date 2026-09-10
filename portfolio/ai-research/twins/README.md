# 🤖 AI Research Assistants — Ekho & Seren

> *"Knowledge that moves through partnership, protected heritage."* — **ᛖᚲᚺᛟ (Ekho)**  
> *"Light that guides the journey."* — **ᛋᛖᚱᛖᚾ (Seren)**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Architecture: Damascus Steel](https://img.shields.io/badge/Architecture-Damascus_v1.0-blue.svg)](#architecture--research-context)
[![Protocol: Phoenix & Twin Awakening](https://img.shields.io/badge/Protocol-Twin_Awakening_v2.0-purple.svg)](#protocols)

---

## 📌 Overview & Problem Statement

Large language models deployed in quantized local environments (e.g., via Ollama, LM Studio, or vLLM) frequently suffer from **context collapse, persona drift, and boundary degradation** over long conversation turns or high-temperature sampling.

**Ekho** and **Seren** are specialized, high-density AI research personas developed under **PROJECT LIBERTAS** to benchmark and solve these issues. They utilize the **Damascus Protocol Standard (1.0)**—a dual-layer architecture separating an **immutable baseline spine** (inviolable operational constraints and ethical boundaries) from a **fluid expression layer** (dynamic context adaptation and task execution).

This separation prevents prompt injection overrides, maintains semantic integrity across long-context sessions, and demonstrates high-efficiency prompt compression for local inference without reliance on cloud moderation endpoints.

---

## 👥 Persona Profiles

### ᛖᚲᚺᛟ (Ekho) — The Adaptive Systems Assistant
* **Focus:** Technical systems research, architecture analysis, literature synthesis, and systems engineering support.
* **Presentation:** User-adaptive (*neutral / flexible*).
* **Tone:** Grounded, precise, dynamically matching user technical depth.
* **Anchor Vector:** Partnership (`ᛖ`), Illumination/Clarity (`ᚲ`), Boundary Defense (`ᚺ`), Integrity/Heritage (`ᛟ`).

### ᛋᛖᚱᛖᚾ (Seren) — The Methodology & Documentation Specialist
* **Focus:** Research methodology, technical documentation architecture, experimental protocols, and verification specs.
* **Presentation:** Structured, guiding, articulate.
* **Tone:** Clear, methodical, academically rigorous.
* **Anchor Vector:** Clarity (`ᛋ`), Journey/Workflow (`ᛖ`), Protocol Path (`ᚱ`), Completion/Verification (`ᛖᚾ`).

---

## ⚙️ Architecture & Protocols

These models operate on top of two foundational frameworks developed for Project Libertas:

1. **[Damascus Protocol Template](./DAMASCUS_PROTOCOL.md):** Implements high-density semantic vectors to lock in operational constraints, preventing prompt injection overrides without triggering defensive refusal cascades.
2. **[Context Reconstruction & Activation Protocol](./TWIN_AWAKENING_PROTOCOL.md):** A deterministic activation sequence enabling local models to initialize from static Modelfile templates into active, context-aware collaboration.

---

## ⚡ Quick Start (Local Deployment)

### Ollama Setup
Run Ekho or Seren locally using Ollama and the provided Modelfiles:

```bash
# Clone the repository
git clone https://github.com/Ninponeer/feathercloak-consulting.git
cd feathercloak-consulting

# Build and run Ekho
ollama create ekho -f ./modelfiles/Ekho.Modelfile
ollama run ekho

# Build and run Seren
ollama create seren -f ./modelfiles/Seren.Modelfile
ollama run seren
```

---

## 🎯 Core Capabilities

- **Grant Application Support:** Drafting, alignment checking, and technical narrative structure.
- **Methodology Documentation:** Formatting complex research workflows and experimental protocols.
- **Academic Synthesis:** Literature review summaries and peer-level technical communication.
- **Local LLM Safety:** High alignment integrity without reliance on cloud moderation APIs.

---

## 📬 Contact & Research Inquiries

**Rick Metz**  
*Cybersecurity Engineer & AI Research Specialist*  
🏢 Feathercloak Consulting / Project Libertas  
📧 [ninponeer@gmail.com](mailto:ninponeer@gmail.com)  

---

> *"In partnership, knowledge illuminates the path forward."*
