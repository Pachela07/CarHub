# AutoMarket

AutoMarket is a small Django 5 app for cataloging cars with brand linkage, photo uploads, price validation, and basic auth (register/login/logout). Built for local development.

Status: Work in progress (development only).

## Features
- Car catalog with brand relation, model, plate, years, price, and optional photo stored under `media/car_manage/`.
- Model search on `/index/` via the `search` query param and the navbar search box.
- Add new cars with a `CarModelForm` that validates minimum price and factory year.
- Basic auth flows using Django's built-in forms: register, login, logout.
- Django admin enabled for data management.

## Tech Stack
- Python 3.12+ (tested on 3.13)
- Django 5.2.7
- SQLite (default)
- Pillow for image handling

## Project Layout
- `manage.py`
- `app/` (`settings.py`, `urls.py`, `templates/skeleton.html`)
- `car_manage/` (`models.py`, `forms.py`, `views.py`, `templates/`)
- `user_accounts/` (`views.py`, `templates/`)
- `media/` (uploaded files, dev only)
- `db.sqlite3` (dev only)

## Setup
1) Create and activate a virtualenv  
   Windows (PowerShell):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
   macOS/Linux:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

2) Install dependencies
   ```
   pip install -r requirements.txt
   ```

3) Migrate the database
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4) Create a superuser (recommended for admin)
   ```
   python manage.py createsuperuser
   ```

5) Run the dev server
   ```
   python manage.py runserver
   ```

Open:
- Index: http://127.0.0.1:8000/index/
- Add car: http://127.0.0.1:8000/new_car/
- Register: http://127.0.0.1:8000/register/
- Login: http://127.0.0.1:8000/login/
- Admin: http://127.0.0.1:8000/admin/

## Media and Static
- `MEDIA_ROOT` and `MEDIA_URL` are set in `app/settings.py` and served in development via `app/urls.py`.
- Uploaded car photos are stored under `media/car_manage/`. Ensure the folder is writable locally.

## Useful Commands
- `python manage.py runserver` - start the dev server
- `python manage.py makemigrations && python manage.py migrate` - apply model changes
- `python manage.py createsuperuser` - create an admin user
- `python manage.py changepassword <username>` - reset a password
- Forgot the admin password but cannot recall the username? Run:
  ```
  python manage.py shell -c "from django.contrib.auth import get_user_model; u=get_user_model().objects.first(); u.set_password('NewStrongPass123!'); u.save(); print('OK')"
  ```

## Development Notes
- URLs are defined in `app/urls.py`.
- Forms and validation live in `car_manage/forms.py`; views in `car_manage/views.py`.
- Templates: base layout in `app/templates/skeleton.html`; pages in `car_manage/templates/` and `user_accounts/templates/`.
- Price validation uses `CarModelForm.clean_value` (minimum 5000). Adjust there if your rules change.

## Troubleshooting
- Pillow is required for `ImageField`; install a matching wheel or build tools if installation fails.
- If running in a headless environment, `tkinter.messagebox` in `user_accounts/views.py` may not display; swap it for Django messages if needed.
