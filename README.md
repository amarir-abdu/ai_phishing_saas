# AI-Powered Phishing Defense SaaS

An AI-powered Software as a Service (SaaS) platform that analyzes emails and messages to detect phishing and scam attempts using machine learning.

This project is designed as a practical, solo-developer friendly cybersecurity + AI system that turns raw email text into intelligent security decisions.

## Project Overview
Phishing is one of the most common and dangerous cyberattacks. Attackers trick users into clicking malicious links, sharing credentials, or installing malware.

AI Phishing Defense SaaS acts like a digital immune system:
- It receives email content.
- It analyzes language patterns and links.
- It predicts how risky the message is.
- It explains the decision.
- It helps users avoid getting tricked.
Instead of static rules, the system learns from real phishing data and improves over time.

## Goals
- Detect phishing emails using machine learning.
- Provide a clear risk score and label.
- Explain why an email is dangerous.
- Be simple enough for a single developer to build and extend.
- Serve as a foundation for a real SaaS product.

## Core Features (Planned)
- AI-based phishing classification.
- Risk scoring (0–100).
- Safe / Suspicious / Phishing labels.
- Explanation engine.
- REST API for scanning emails.
- Web dashboard (later stage).
- Logging and history of scans.

## Pipeline:
```
Input Email → Feature Extraction → ML Model → Risk Score → Explanation → Storage → UI
```

## Project Structure
```
ai_phishing_saas/
│
├── data/ # Datasets
├── model/ # Training scripts
├── api/ # FastAPI service
├── saved_models/ # Trained ML models
├── docs/ # Documentation
├── project_plan.md
└── README.md
```

## Getting Started
### Clone Repository
```
git clone <your-repo-url>
cd ai_phishing_saas
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Train the Model
```
cd model
python train_model.py
```
### Run API Server
```
cd api
uvicorn main:app --reload
```
### Test API
```http://127.0.0.1:8000/docs```

## Contribution
This project is built for learning and experimentation. Ideas, improvements, and extensions are welcome.

## License
MIT