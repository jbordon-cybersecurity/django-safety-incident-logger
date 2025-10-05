```bash
# 🧩 Safety Incident Logger

A simple Django web application to record, view, and manage safety incidents.  
Built as a practical learning project to strengthen my Python, Django, and secure web development skills.

---

## 🚀 Features
- Add and view incidents with fields such as:
  - Title  
  - Description  
  - Category  
  - Severity  
  - Country Issued  
- Stores data securely using Django ORM (SQLite).  
- Includes CSRF protection and Django’s built-in admin interface.

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/<your-username>/django-safety-incident-logger.git
cd django-safety-incident-logger

2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies
pip install django

4. Apply migrations and start the development server
python manage.py migrate
python manage.py runserver


Then visit http://127.0.0.1:8000/
 in your browser.

## 🧠 Learning Outcomes

Through this project, I:

Strengthened my understanding of Django models, views, and templates.

Practiced secure coding and defensive programming principles.

Gained experience managing version control with Git and GitHub.

Improved my ability to turn an idea into a functional web application.

👤 Author

Jose Bordon
Cybersecurity & Forensics Student @ Edinburgh Napier University

---

## 📝 License & Copyright

© 2025 Jose Bordon.  
This project is shared publicly for educational and portfolio purposes.  
You may view and reuse the code for learning, but please give appropriate credit.  
Commercial use or redistribution without permission is not allowed.
