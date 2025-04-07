## Future Improvement updated

| Feature                           | Status |
| --------------------------------- | :----: |
| CRUD                              |   ✅   |
| Add/Change database to Postgresql |        |

---

# 📦 Inventory Management System

A simple and scalable Inventory Management System built with **Flask** (Python) and **Firebase Firestore** as the database. It helps users manage product data with clean UI and full CRUD capabilities.

---

## 🧠 Problem Description

Managing inventory manually or with spreadsheets can lead to errors, inefficiencies, and difficulties in scaling. This project provides a centralized, cloud-based inventory management system to solve those problems — making it easier to track, update, and analyze inventory data in real-time from anywhere.

---

## 🚀 Key Features

- 📋 Add, update, and delete inventory items
- 🔍 View product list with optional search
- 📦 Track id, name, quantity, description
- ☁️ Real-time sync with Firebase Firestore
<!-- - 🔐 Optional login with Firebase Authentication
- 📊 Dashboard with summary statistics _(optional)_ -->

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: Firebase Firestore
- **Frontend**: HTML, CSS, JavaScript (with Jinja2 templating)
- **Others**: Python Dotenv
<!-- - **Authentication**: Firebase Authentication _(optional)_
- **Deployment**: Compatible with Heroku, Render, etc. -->

---

## 🏗️ System Design

User ↓ Flask App (Backend + Views) ↓ Firebase Firestore (Cloud Database)

**Entity Structure:**

- `Inventory Collection`
  - `Document (Product ID)`
    - `name`
    - `stock`
    - `description`

---

## 📁 Project Structure

```
inventory-management/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── routes.py
├── .flaskenv
├── .gitignore
├── main.py
├── README.md
└── requirements.py
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/inventory-management.git
   cd inventory-management
   ```
2. **Create and activate virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app**

   ```bash
   flask run
   ```

5. **Access locally**
   ```cpp
   http://127.0.0.1:5000
   ```

---

## 🧪 Future Improvements

- ✅ Firebase Authentication integration

<!-- - ✅ Export data to CSV or Excel

- 📊 Analytics dashboard using charts

- 📷 Product image uploads via Firebase Storage

- 📱 PWA support for mobile use

- 👥 Multi-user access with roles -->

---

## 📌 Learnings

- Integration of Flask with a cloud-based NoSQL database

- Working with Firebase Firestore

- Secure environment variable handling

- Jinja2 templating and form-based data operations

- Modular Flask app structure
