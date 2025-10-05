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

### Clone the repository
```bash
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

---

## 🛠️ Technologies Used
- **Python 3**
- **Django**
- **HTML/CSS (Django Templates)**
- **SQLite** (default database)

---



