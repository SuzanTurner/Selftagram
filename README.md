# 📸 Selfstagram

**Selfstagram** is a Django-based web application that allows users to register, log in, and upload their personal photos. Each user gets their own private gallery — simple, clean, and secure.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 🖼️ Upload and view images
- 🧑‍🦱 User-specific galleries
- 📦 Media file handling via `MEDIA_ROOT` and `MEDIA_URL`
- 🎨 Styled with Bootstrap for a responsive UI

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (default)

---

## 📂 Project Structure

```
selfstagram/
├── selfstagram/ # Main Django settings
├── myapp/ # App containing views, models, forms
├── templates/ # HTML templates
├── media/ # Uploaded images
├── static/ # Static files (optional)
├── manage.py
└── README.md
```


---

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



