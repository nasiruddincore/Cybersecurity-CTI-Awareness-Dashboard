# 🛡️ Cybersecurity Awareness & Threat Intelligence Dashboard

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A defensive cybersecurity dashboard that combines threat intelligence analysis with human-centric security awareness. This project ingests, validates, and visualizes synthetic Indicators of Compromise (IOCs) and vulnerabilities, scoring organizational risk while delivering educational nudges to users.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [System Objectives](#-system-objectives)
- [Features](#-features)
- [Folder Structure](#-folder-structure)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Ethical Disclaimer](#-ethical-disclaimer)

---

## 📌 Project Overview
Modern Security Operations Centers (SOCs) blend technical threat intelligence with internal telemetry. This platform bridges the gap between raw threat data and human behavior by pairing actionable IOC analysis with awareness training to reduce phishing clicks and incident response times.

---

## ⚠️ Problem Statement
* **Alert Fatigue:** SOC analysts are overwhelmed by raw indicators without context, risk prioritization, or confidence scoring.
* **Human Vulnerability:** Technical defenses fail when users cannot recognize social engineering or phishing attempts.
* **Disconnected Systems:** Threat intelligence and security awareness are often siloed, preventing a unified defensive posture.

---

## 🎯 System Objectives
1. **Threat Analysis:** Validate and enrich synthetic IOCs (IPs, Domains, Hashes, CVEs).
2. **Risk & Confidence Scoring:** Differentiate between the potential impact of a threat (Risk) and the reliability of the intelligence (Confidence).
3. **SOC Investigation Workflow:** Provide a clean, prioritized view of active threats and historical activity.
4. **Security Awareness:** Test and educate users on critical defensive hygiene (e.g., Phishing, MFA).

---

## 🚀 Features
* **Automated Data Generation:** Automatically generates a robust dataset of safe, synthetic threat records.
* **IOC Validation Engine:** Syntactically verifies indicator types (IPv4, Domains, CVE IDs) before searching the database.
* **Real-Time SOC Dashboard:** Tracks total records, critical severity items, and active investigations.
* **Interactive Awareness Center:** Built-in quizzes to evaluate and improve user response to common cyber threats.

---

## 📂 Folder Structure
```text
Cybersecurity-CTI-Dashboard/
│
├── data/                            
│   └── synthetic_threats.csv        # Auto-generated synthetic telemetry log
│
├── app.py                           # Core Streamlit application & backend logic
├── requirements.txt                 # Project dependencies
├── .env.example                     # Environment variables template
├── .gitignore                       # Git exclusion file
└── README.md                        # Project documentation