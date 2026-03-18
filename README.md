# Medical Diagnosis Expert System (AI — 2026)

An academic-focused, web-based expert system designed to demonstrate AI forward chaining inference for medical diagnosis. This project leverages Django for the backend and a modern glassmorphism UI architecture for the frontend.

## 🚀 Key Features

- **AI Inference Engine**: Implements a forward chaining algorithm in Python to match user symptoms against a clinical knowledge base.
- **Iterative Inference & Dynamic Suggestions**: The UI actively suggests relevant symptoms based on current selections to guide the user toward a narrower diagnosis.
- **Explainability Facility**: Integrated "Reasoning Tooltips" that show exactly how many symptoms matched versus the total required for any given diagnosis.
- **Exportable Case Reports**: Allows users to download a professional diagnostic summary as a text file for documentation.
- **Knowledge Base Manager**: A dedicated administration interface to add/edit diseases, symptoms, and diagnostic rules without leaving the application.
- **Static Knowledge Base**: Seeded data featuring Common Cold, Flu, Malaria, Typhoid, Food Poisoning, and Allergies.

## 🛠️ Technology Stack

- **Backend**: Python 3.9+, Django 4.2+
- **Database**: SQLite3
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 5, Bootstrap Icons
- **Typography**: Google Fonts (Outfit)

## 📋 Project Structure

```text
medical_expert_system/
├── diagnoses/               # Core Django Application
│   ├── inference_engine.py  # AI Logic (Forward Chaining)
│   ├── models.py            # Knowledge Base Schema (Symptom, Disease, Rule)
│   ├── seed/                # Database Seeding Scripts
│   ├── static/              # Modern CSS Theme & Assets
│   └── templates/           # Glassmorphism HTML Layouts
├── expert_system/           # Main Project Configuration
├── manage.py                # Django CLI
└── README.md                # This Guide
```

## ⚙️ Setup & Execution

### 1. Environment Setup
Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment:

```bash
# macOS/Linux
python3 -m venv env
source env/bin/activate

# Windows (Command Prompt)
python -m venv env
env\Scripts\activate

# Windows (PowerShell)
python -m venv env
.\env\Scripts\Activate.ps1
```

### 2. Dependency Installation
Install the necessary requirements (Django is the primary dependency):

```bash
pip install django
```

### 3. Database Initialization
Run the migrations to set up the SQLite database schema:

```bash
python3 manage.py migrate
```

### 4. Seed the Knowledge Base
Run the included seed script to populate the database with symptoms, diseases, and diagnostic rules:

```bash
python3 manage.py shell -c "from diagnoses.seed import seed_data; seed_data.run()"
```

### 5. Start the Server
Run the development server and navigate to `http://127.0.0.1:8000/diagnose/`:

```bash
# macOS/Linux
python3 manage.py runserver

# Windows
python manage.py runserver
```

### 6. Login & UI Quick Access
- Visit `http://127.0.0.1:8000/accounts/login/` to sign in.
- If you go to `http://127.0.0.1:8000/admin/login/`, it redirects to the custom app login.
- After login, the navbar includes: `Welcome <username>`, `User Manual`, `KB Manager` (staff only), `Logout`, and `AI Assignment, 2026`.
- The in-app user manual is at `http://127.0.0.1:8000/diagnose/manual/`.

## 🎓 Academic Context
This project was developed as an **AI Assignment Submission (2026)** to illustrate the application of Rule-Based Expert Systems in healthcare diagnostics. It focuses on the transparency of the inference process, providing clear feedback on why a specific diagnosis was suggested.