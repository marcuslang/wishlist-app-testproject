# Wishlist App (test project)

> ⚠️ This is just a test/demo project — not production-ready.

A minimal wishlist app: log in, create your wishlist, add items (text + optional
URL, e.g. a link to Amazon), give the wishlist a title, and share it with others
via a public link.

## Tech Stack

- Backend: **Django 3.2**, **Python 3.10**
- Frontend: **jQuery**
- Database: **SQLite** (local)

## Features

- Sign up / log in / log out (Django's built-in auth)
- Each user has one wishlist with an editable title
- Add and delete wishlist items (text + optional URL)
- Share your wishlist via a public, unguessable link (`/wishlist/shared/<token>/`)
  — no login required to view

## Getting Started

### Requirements

- Python 3.10

### Setup

```bash
git clone git@github.com:marcuslang/wishlist-app-testproject.git
cd wishlist-app-testproject

python3.10 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

### Access

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/ (create a superuser with
  `python manage.py createsuperuser`)

## Project Structure

- `wishlist_project/` — Django project settings/urls
- `wishlist/` — the wishlist app (models, views, forms, templates)
- `db.sqlite3` — local SQLite database (not committed)
