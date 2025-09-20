# 🍳 Django Recipe Sharing App

A **web-based Recipe Sharing Application** built with **Django**.  
Users can **browse, share, and comment** on recipes using **server-rendered HTML pages**.

## 📖 Description

This is a **traditional Django project** that renders **HTML templates** for all pages.  
Users can:  

- Share their own recipes  
- Browse recipes submitted by others  
- Search recipes by name or category  
- View detailed recipe instructions  
- Comment on others’ recipes  

The project uses **Django ORM** for database operations and **templates for UI**, making it beginner-friendly and easy to extend.

## ⚡ Features

- **Browse Recipes** – View all recipes shared by users.  
- **Search Recipes** – Search recipes by name, category, or keywords.  
- **Recipe Details** – View full recipe details including ingredients and instructions.  
- **Add Recipes** – Submit your own recipes via HTML forms.  
- **Comment on Recipes** – Users can comment on others’ recipes, fostering interaction.  
- **Edit / Delete Recipes** – Update or remove your own recipes     
- **Database Integration** – Recipes and comments stored using Django ORM with SQLite.  
- **Server-rendered HTML** – All pages rendered using Django templates.  
- **Recipe Sharing Platform** – Encourages community interaction through shared recipes and comments.  

## 🚀 Installation & Running Locally

1. **Clone the repository**:

git clone https://github.com/saba-imtiaz/django-recipeproject.git
cd django-recipeproject

2. **Create and activate a virtual environment**:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

3. **Install dependencies**:

pip install django

4. **Apply migrations**:

python manage.py migrate

5. **Run the development server**:

python manage.py runserver

## 🛠 Tech Stack

* **Django 4.x** – Backend and server-side rendering
* **Python 3.x** – Core language
* **SQLite** – Default development database
* **HTML/CSS** – Frontend templates

## 👨‍💻 Author

**Saba Imtiaz** – [GitHub Profile](https://github.com/saba-imtiaz)
