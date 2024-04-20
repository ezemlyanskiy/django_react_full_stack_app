# Django React Full Stack App

A simple django react full stack application to manage notes.

## Getting Started

First of all:

```bash
git clone git@github.com:ezemlyanskiy/django_react_full_stack_app.git
cd django_react_full_stack_app
python3 -m venv venv
python -m pip install -U pip
python -m pip install -r requirements.txt
```

Open two terminals and run backend and frontend:

```bash
cd backend
cat .env.example > .env  # and fill it out
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

```bash
cd frontend && npm run dev
```

Open your browser at http://127.0.0.1:8000.
