# INSE-6140 – Vulnerability Assessment Project

This repository contains the project files and documentation for a vulnerability assessment conducted on the WordPress plugin **Really Simple SSL v9.1.1**, as part of the coursework for **INSE 6140 – Security Assessment** at Concordia University.

## 🔍 Project Overview

The project focuses on identifying and exploiting a critical **authentication bypass vulnerability** in the Two-Factor Authentication (2FA) onboarding process of the Really Simple SSL plugin. The exploit allows unauthorized users to gain administrative access via a vulnerable REST API endpoint.

## 🧪 Testing Environment

- **Platform**: Kali Linux
- **Deployment**: Docker Compose setup with WordPress 6.4.3 and MySQL 8.0
- **Vulnerable Plugin**: Really Simple SSL v9.1.1

## 🛠️ Tools Used

- **Static Analysis**: Semgrep, PHPStan, Snyk
- **Dynamic Testing**: Burp Suite, Browser DevTools
- **Exploitation**: Custom Python script (`exploit.py`)
- **Scanning**: WPScan, OWASP ZAP

## 📁 Contents

- `exploit.py`: Python script to bypass 2FA and retrieve admin session cookies.
- `docker-compose.yml`: Environment setup for WordPress and MySQL containers.
- `report/`: Contains the final vulnerability assessment reports from different tools.
- `Code/`: Contains files reated to vulnerable and fixed code.


## 👥 Team Members

- Sarath Kumar Manchineni – 40153139  
- Jyothi Sree Kondru – 40291701  
- Raghu Pavan Annam – 40303699

## 📄 License

This repository is intended for academic purposes only. Do not use the techniques or tools demonstrated here on systems you do not own or have explicit permission to test.

