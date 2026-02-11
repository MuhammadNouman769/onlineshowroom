# 1 Go to your project folder
cd ~/Nouman\ Data/projects/cardekho

# 2 Create Django apps
python manage.py startapp cars
python manage.py startapp users

# 3 Create virtual environment & activate
python3 -m venv .venv
source .venv/bin/activate

# 4 Install Django & DRF
pip install django djangorestframework

# 5 Verify Django installation
python -m django --version

# 6 Run initial migrations
python manage.py migrate

# 7 Git initialization & remote setup
git init
git remote add origin https://github.com/MuhammadNouman769/onlineshowroom.git

# 8 Create .gitignore
echo "*.pyc
__pycache__/
db.sqlite3
.venv/
*.log
.env" > .gitignore

# 9 Stage & commit initial project
git add .
git commit -m "Initial commit: Django project with apps and .gitignore"

# 10 Push to GitHub
git branch -M main
git push -u origin main

# 11 Create requirements.txt
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt"
git push

# 13 Create README.md
echo "# Online Showroom

**Project:** Django-based Online Car Showroom
**Author:** Muhamman Nouman
**Technology Stack:** Python, Django, Django Rest Framework (DRF), SQLite

## Project Overview
Online Showroom ek web application hai jahan users cars dekh, filter aur purchase requests bhej sakte hain. Backend Django + DRF pe bana hai aur APIs provide karta hai for frontend or third-party apps.

### Main Features:
- User registration & authentication (users app)
- Car listing, filter, search (cars app)
- RESTful API endpoints
- Admin panel for managing cars & users

## Project Setup
1. Clone repository:
git clone https://github.com/MuhammadNouman769/onlineshowroom.git
cd onlineshowroom

2. Create virtual environment & activate:
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run development server:
python manage.py runserver

6. Access in browser:
http://127.0.0.1:8000/

## Apps in Project
- users: User authentication & profile management
- cars: Car listing, details, filtering

## API Endpoints (Sample)
| Endpoint | Method | Description |
|----------|-------|-------------|
| /api/users/register/ | POST | User registration |
| /api/users/login/ | POST | User login |
| /api/cars/ | GET | List all cars |
| /api/cars/<id>/ | GET | Car details by ID

## Notes
- .venv/ and db.sqlite3 excluded in .gitignore
- Activate virtual environment before running server
- To add new packages:
pip install package_name
pip freeze > requirements.txt
" > README.md

# 13 Add README.md and push
git add README.md
git commit -m "Add full professional README.md"
git push