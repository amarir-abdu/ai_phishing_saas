# Project Plan: AI-Powered Phishing Defense SaaS

## 1. System Overview
What Does the System Do?

The system is an AI-powered SaaS platform that analyzes emails and messages to detect phishing and scam attempts before users interact with them.
In simple terms, it acts like a digital immune system for communication:
- It receives email content (subject, body, sender, and links).
- It analyzes the text and URLs using machine learning.
- It calculates a risk score that represents how dangerous the message is.
- It classifies the message as Safe, Suspicious, or Phishing.
- It explains why the message is risky.
- It stores results so users can review past threats.
Instead of relying only on static rules, the system learns patterns from real phishing data and adapts over time.

## 3. Data Flow
The system data flow looks like this:
1. User submits an email or connects an inbox.
2. Frontend sends email data to the Backend API.
3. Backend forwards content to the AI Engine.
4. Feature Extraction converts text + URLs into vectors.
5. ML Models predict risk scores.
6. Results return to Backend.
7. Backend stores data in Database.
8. Frontend displays risk, label, and explanation.
9. User feedback flows back for learning.
Types of data moving around:
- Email subject and body
- Sender information
- URLs
- Feature vectors
- Risk scores
- Labels (safe / phishing)
- Explanations
- User feedback
The system always transforms raw text → features → predictions → decisions → stored insight.

## 4. System Components
The system is split into logical services:
1. Frontend (Web Dashboard)
Displays scan results, risk scores, alerts, and history to the user.
2. API Backend
Handles authentication, receives scan requests, talks to the AI engine, and stores results.
3. AI / ML Engine
Processes text and URLs, runs machine learning models, and produces risk predictions.
4. Feature Extraction Layer
Converts raw email data into numerical features for models (text vectors, URL stats, behavior signals).
5. Database
Stores users, scanned emails, predictions, feedback, and logs.
6. Integration Layer (Later Stage)
Connects to email providers (Gmail, Outlook) to ingest messages automatically.
Each component is independent but connected through APIs.

## 5. MVP Scope
### What's Included:
- A simple web form to submit email subject + body.
- A backend API endpoint /scan.
- A machine learning model trained on phishing text.
- A risk score output (0–100).
- A label: Safe / Phishing.
- A basic explanation of the decision.
- A small database to store scans.

### What's NOT Included (Future):
- Gmail integration
- Billing
- Mobile apps
- Multi-user organizations
- Complex dashboards

## 6. Development Phases

### Phase 1: Core ML Engine (Weeks 1-2)
**Goal:** Build and validate a machine-learning model that can classify emails as safe, suspicious, or phishing with a meaningful risk score.

**Tasks:**
- [X] Collect and clean phishing + legitimate email datasets.
- [X] Preprocess text (lowercase, tokenize, remove noise, normalize).
- [X] Train baseline ML model (Logistic Regression / Random Forest / LightGBM).
- [X] Evaluate accuracy, precision, recall, F1 score.
- [ ] Create a simple prediction script for testing.

### Phase 2: API Backend (Weeks 3-4)
**Goal:** Expose the ML model through a secure and scalable API service.

**Tasks:**
- [ ] Build FastAPI backend structure.
- [ ] Load trained model at startup.
- [ ] Run inference and return risk score + label.
- [ ] Add request validation and error handling.
- [ ] Add logging for scans.
- [ ] Add basic authentication (API key or token).

### Phase 3: Frontend MVP (Weeks 5-6)
**Goal:** Create a simple user interface where users can submit emails and view results.

**Tasks:**
- [ ] Build minimal UI (HTML + CSS + JS or React).
- [ ] Create form to submit subject + body.
- [ ] Connect frontend to API endpoint.
- [ ] Display risk score, label, and explanation.
- [ ] Add loading and error states.
- [ ] Store scan history for the user session.

### Phase 4: Enhancement (Weeks 7+)
**Goal:** Improve intelligence, usability, and product readiness.

**Tasks:**
- [ ] Add URL analysis and domain reputation checks.
- [ ] Improve ML model using deep learning (BERT / transformers).
- [ ] Add feedback loop for retraining.
- [ ] Add database persistence for users and scans.
- [ ] Add user authentication system.
- [ ] Add dashboard analytics.
- [ ] Prepare deployment (Docker + cloud hosting).

## 7. Technology Stack
### Backend:
- Python
- FastAPI
- Uvicorn
- Pydantic
- JWT / API Key Auth

### ML/AI:
- Scikit-learn
- Pandas
- NumPy
- NLTK / SpaCy
- Transformers (optional later)
- TF-IDF Vectorizer

### Database:
- SQLite (MVP)
- PostgreSQL (production)
- SQLAlchemy ORM

### Frontend:
- HTML / CSS / JavaScript
- React (optional upgrade)
- Fetch / Axios

## 8. Success Metrics for MVP
- [ ] User can submit email text
- [ ] System returns risk score in < 2 seconds
- [ ] Model achieves > 85% accuracy on test set
- [ ] API handles invalid input gracefully.
- [ ] Results are stored and retrievable
- [ ] UI shows label + explanation clearly.
- [ ] Backend logs each scan.