# 📸 Selfstagram

**Selfstagram** is a Django-based web application allowing users to register, log in, and upload photos. 

Each user gets their private gallery — simple, clean, and secure.

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 🖼️ Upload and view images
- 🧑‍🦱 User-specific galleries
- 📦 Media file handling via `MEDIA_ROOT` and `MEDIA_URL`
- 🎨 Styled with Bootstrap 

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (default)

## 📂 Project Structure

```
selfstagram/
├── selfstagram/ 
├── myapp/ 
├── templates/
├── media/ 
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/selfstagram.git
cd selfstagram
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```
python manage.py createsuperuser
```

### 6. Run the server
```
python manage.py runserver
```
---

## Author - Yadhnika Wakde (ThE_CrUd_LaDy)



