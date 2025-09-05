# 🗨️ Django Chatbot with Groq GenAI

This project is a **chatbot application** built with **Django** and integrated with **Groq GenAI** for intelligent responses.  
It includes **user authentication**, persistent **chat history storage**, and a **clean front-end** using vanilla CSS and Bootstrap.  

---

## 🚀 Features
- 🔐 **User Authentication** – Sign up, log in, and manage personal accounts.  
- 💬 **Chat with AI** – Powered by **Groq GenAI** for fast and contextual responses.  
- 🗄️ **Database Integration** – Store and retrieve chat history per user using Django’s ORM.  
- 🎨 **UI Design** – Clean layout with **vanilla CSS** + **Bootstrap** for responsiveness.  
- 🛠️ **Django Admin Panel** – Manage users and chats via Django’s built-in admin.  

---

## 🛠️ Tech Stack
- **Backend:** Django 5.2.6 (Python)  
- **Frontend:** HTML, Vanilla CSS, Bootstrap  
- **AI Model:** Groq GenAI API  
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)  

---

## 📦 Installation
1. Clone the repository  
   ```bash
   git clone https://github.com/debonilsaha21/Django-Chatbot.git
   cd django-chatbot
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
2. GROQ_API_KEY=your_api_key_here
   ```bash
   python manage.py migrate
   python manage.py runserver
## ▶️ Usage
  Visit http://127.0.0.1:8000
  Register/Login to your account
  Start chatting with the AI!
