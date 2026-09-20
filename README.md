<div align="center">

# ⚡ DISCORD TOKEN MANAGER v1.0

**An advanced, lightweight, and modern Flask-powered web utility for managing and verifying Discord tokens with real-time analytics.**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Author](https://img.shields.io/badge/author-Haribo-7289da.svg?style=for-the-badge)](https://github.com/)
[![Version](https://img.shields.io/badge/version-1.0-brightgreen.svg?style=for-the-badge)](https://github.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [Configuration](#-configuration) • [Usage](#-usage) • [Disclaimer](#-disclaimer)

</div>

---

## ✨ Features

### 🔍 Token Verification & Scanning
- **Real-time API Validation:** Instantly pings Discord API (`/users/@me`) to verify token validity.
- **Detailed Account Analytics:** Extracts username, discriminator, unique ID, email, phone status, and precise account creation date derived from Snowflake IDs.
- **Nitro Status Checker:** Automatically detects active subscriptions and Nitro perks.

### 🚀 Management & Utility
- **One-Click Quick Login:** Seamless copy-to-clipboard and login helper integration.
- **Clean Dark Dashboard:** Designed with a sleek, minimalist Discord-inspired dark mode UI.
- **Fast Single-Input Workflow:** Streamlined interface designed for rapid testing and management without browser lag.

---

## 📸 Interface Preview

```text
+-----------------------------------------------------------------------------------+
|  ⚡ DISCORD TOKEN MANAGER -- Made By Haribo                                [-][o][x]  |
+-----------------------------------------------------------------------------------+
| [ Enter token here...                      ] [ Check Token ]                      |
+-----------------------------------------------------------------------------------+
| Scanned Accounts                                                                  |
| # | Username         | Nitro       | Creation Date       | Action             |
|---|------------------|-------------|---------------------|--------------------|
| 1 | Haribo#0001      | Active 🚀   | 2024-01-15 12:30:00 | [Copy Token & Login] |
+-----------------------------------------------------------------------------------+
