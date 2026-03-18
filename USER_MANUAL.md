# Medical Diagnosis Expert System - User Manual

## 1. Introduction
Welcome to the Medical Diagnosis Expert System. This application is a Django-based rule-driven AI diagnostic support tool designed for academic demonstration and structured medical inference. It helps users input symptoms, receive probable diagnoses with confidence scores, and export professional case reports.

### 1.1 Audience
- Healthcare students and faculty using the tool for learning.
- Medical experts managing diagnostic knowledge rules.
- QA and testers validating clinical reasoning logic.

### 1.2 Scope
This manual covers:
- System requirements and setup
- Patient diagnosis workflow
- Knowledge Base Manager usage
- Export report features
- Administrative controls and troubleshooting

---

## 2. System Overview
The system has two primary functional modules:
1. **Diagnosis Interface** (`/diagnose/`) - where users select symptoms and view AI-generated matches.
2. **Knowledge Base Manager** (`/kb-manager/`) - where authorized staff maintain diseases, symptoms, and diagnostic rules.

### 2.1 Core Components
- **Symptom Selection**: Multiple checkboxes for symptom input.
- **Inference Engine**: Forward chaining algorithm in `diagnoses/inference_engine.py` matching symptom sets to rules.
- **Dynamic Suggestions**: Real-time recommended symptoms based on selected symptoms.
- **Reasoning Tooltips**: Explains matched vs missing symptoms for each diagnosis.
- **Knowledge Base Manager**: Add disease/symptom/rule interface for trained experts.
- **Exportable Case Report**: Download diagnosis summary as a `.txt` file.

---

## 3. Getting Started

### 3.1 Prerequisites
- Python 3.9+
- Django 4.2+
- SQLite3 (default)

### 3.2 Installation
1. Clone the repository.
2. Create and activate your virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Seed initial data:
   ```bash
   python manage.py shell -c "from diagnoses.seed import seed_data; seed_data.run()"
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
7. Open the app in your browser:
   - Diagnosis page: `http://127.0.0.1:8000/diagnose/`
   - Knowledge base manager (staff only): `http://127.0.0.1:8000/kb-manager/`

---

## 4. User Workflow: Generate a Diagnosis

### 4.1 Accessing the Diagnosis Page
Open `http://127.0.0.1:8000/diagnose/`.

### 4.2 Enter Symptoms
1. On the `Symptom Input` card, select all symptoms the patient reports.
2. As symptoms are selected, the `Recommended to Check` section automatically appears with symptom suggestions.
3. Optionally click suggestion chips to auto-select additional symptoms.

### 4.3 Run Inference
Click **Analyze Symptoms**.
The system returns a ranked list of potential diagnoses with match confidence and reasoning.

### 4.4 Interpreting Results
For each inference result:
- **Disease Name**: Predicted condition.
- **Confidence Badge**: `high`, `medium`, or `low` match percentage.
- **Progress Bar**: Visual score based on matched and total required symptoms.
- **Matched Symptoms**: Confirmed symptoms found in the patient.
- **Missing Symptoms**: Additional required symptoms not provided.
- **Reasoning Tooltip**: Hover info icon to see exact matching count required by the rule.

### 4.5 Export Case Report
Click **Export Report** to download a plain text case report with:
- Timestamp
- Selected symptoms
- Each diagnosis, confidence, matched symptoms, and missing symptoms.

---

## 5. Knowledge Base Manager
The Knowledge Base Manager is restricted to staff users. Superusers can manage core inference rules.

### 5.1 Access Control
- Only authenticated users with staff privileges can access `/kb-manager/`.
- Only superusers can add/edit diagnostic rules.

### 5.2 Manage Diseases
1. Go to the **Diseases** tab.
2. Click **Add Disease**.
3. Enter disease name and optional description.
4. Submit to save.

### 5.3 Manage Symptoms
1. Go to the **Symptoms** tab.
2. Click **Add Symptom**.
3. Enter symptom name.
4. Submit to save.

### 5.4 Manage Diagnostic Rules (Superusers)
1. Go to the **Diagnostic Rules** tab.
2. Click **Add Rule**.
3. Select a target disease.
4. Select one or more symptoms to build the rule.
5. Check the verification checkbox to confirm clinical accuracy.
6. Submit to create/update the rule.

### 5.5 Rule Logic Preview
The interface displays an `IF <symptoms> THEN <disease>` preview to verify correctness before saving.

---

## 6. Administration and Data Maintenance

### 6.1 Django Admin
For full CRUD and bulk edits, use Django Admin:
1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
2. Go to `http://127.0.0.1:8000/admin/`.
3. Manage Diseases, Symptoms, and Rules directly.

### 6.2 Knowledge Base Quality
- Follow standard clinical guidelines before adding rules.
- Ensure each disease-rule has symptoms that reflect real diagnostic pathways.
- Keep symptoms consistent (e.g., avoid synonyms unless normalized).

---

## 7. Troubleshooting

### 7.1 No Diagnoses Returned
- Confirm at least one symptom is selected.
- If no rules match, add or update rules for the disease pathway.
- Check rule symptoms include the selected symptoms.

### 7.2 Staff Manager Not Accessible
- Verify `is_staff=True` in your user profile.
- For rule creation, ensure your user is a superuser.

### 7.3 Incorrect Confidence Scoring
- Confidence is derived from matched vs required symptoms per rule.
- Adjust rule symptom sets if specificity is too broad.

### 7.4 App Startup Fails
- Confirm Python 3.9+ is active.
- Re-run migrations and seed script.
- Check `db.sqlite3` permissions and delete stale migrations only if needed.

---

## 8. Glossary
- **Symptom**: Observable sign or patient-reported complaint.
- **Rule**: One disease and its required symptom set used by the inference engine.
- **Forward Chaining**: Rule-based logic where input facts trigger conclusions.
- **Superuser**: Admin-level account with rule editing privileges.
- **Staff**: User with access to admin-like pages (but not necessarily superuser-only operations).

---

## 9. Release Notes & Versioning
- Version: `1.0.0` (Academic Demonstration)
- Release date: March 2026
- Future enhancements: user authentication improvements, multi-rule confidence blending, CSV import/export for KB data.

---

## 10. Contact & Support
For issues, use project maintainers and repository issues list. Document expected inputs and error behavior to expedite fixes.

---

## 11. Appendices
### A. Security Best Practices
- Do not expose superuser credentials in production.
- Use HTTPS for deployed systems.
- Validate input and restrict APIs.

### B. Development Notes
- Inference logic is in `diagnoses/inference_engine.py`.
- Symptom form is in `diagnoses/forms.py`.
- Database models in `diagnoses/models.py`.
- Frontend templates in `diagnoses/templates/diagnoses/`.
