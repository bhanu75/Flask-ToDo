# 📝 Flask ToDo App

A minimal yet colorful and deadline-aware **ToDo web app** built using Python & Flask. This project supports task creation, deletion, deadlines, and detail views with a dark theme-friendly UI.

## 🌐 Live Demo

🔗 [View Live App](https://flask-todo-8q86.onrender.com)

## 📸 Screenshots

_Add your screenshots here._



## ✅ Features

- Add new tasks with title, details, and deadline
- View list of all tasks
- Click task title to view full details
- Delete individual tasks
- Clear all tasks at once
- Colorful dark-themed UI

---

## 🚀 Technologies Used

- Python 3
- Flask (Backend Framework)
- HTML5 / CSS3 (Frontend)
- UUID (for unique task IDs)
- Render.com (Deployment)

---

## 💻 Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/bhanu75/Flask-ToDo.git
cd Flask-ToDo
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Then open your browser: [http://localhost:5000](http://localhost:5000)

---

## ☁️ Deployment (on Render)

- This app is deployed on [Render.com](https://render.com) using GitHub integration
- Config includes:
  - `render.yaml`
  - `requirements.txt`
  - `app.py`

---

## 🧠 My Learning Experience

This was my **first full project using Flask**. I originally thought ToDo apps are static, but I realized the importance of backend when handling data like tasks, deadlines, and IDs. Initially, I struggled with errors like "Internal Server Error" because of small mistakes like wrong template names (`details.html` vs `detail.html`). Also, I learned that GitHub mobile apps have limited upload capabilities and that we need to use **web service**, not static site, on Render for Python apps.

Overall, this project helped me understand:
- The importance of routing and template structure in Flask
- How to handle user inputs with forms and POST methods
- How backend logic differs from static frontend pages
- Deploying dynamic apps on free cloud services

---

## 🙏 Special Thanks

To all the resources and docs that helped me along the way!

---
