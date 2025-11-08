# Car Manage

A simple Django app to manage cars, with brand linkage, model years, price validation, image uploads, and an admin interface.

Status: Work in progress (development only).

## Features

- Car catalog with brand (FK), model, years, plate, value, and photo.
- Search by model via query param `search` on the index page.
- Add cars using a `ModelForm` with basic validations.
- Image uploads saved under `media/car_manage/`.
- Django admin for data management.

## Tech Stack

- Python 3.12+/3.13+
- Django 5.x
- SQLite (default)

## Project Layout

- `manage.py`
- `app/`
  - `settings.py`, `urls.py`, `templates/skeleton.html`
- `car_manage/`
  - `models.py`, `views.py`, `forms.py`, `admin.py`, `templates/`

## Setup

1) Create and activate a virtualenv (Windows PowerShell)

```
python -m venv .venv
.venv\Scripts\activate
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

4) Run the dev server

```
python manage.py runserver
```

Open:

- Index: http://127.0.0.1:8000/index/
- Add car: http://127.0.0.1:8000/new_car/
- Admin: http://127.0.0.1:8000/admin/

## Admin Access

- Create a superuser:

```
python manage.py createsuperuser
```

- Forgot the admin password:

```
python manage.py changepassword admin
```

If you don’t remember the username, you can reset via shell:

```
python manage.py shell -c "from django.contrib.auth import get_user_model as g; U=g(); u=U.objects.first(); u.set_password('NewStrongPass123!'); u.save(); print('OK')"
```

## Media & Static

- Media is enabled in `app/settings.py` (`MEDIA_ROOT` and `MEDIA_URL`) and served during development via `app/urls.py`.
- Uploaded car photos are stored under `media/car_manage/`.

## Development Notes

- URLs are defined in `app/urls.py` as `index` and `new_car`.
- Forms live in `car_manage/forms.py` and use `ModelForm`.
- Templates:
  - Base: `app/templates/skeleton.html`
  - Pages: `car_manage/templates/index.html`, `car_manage/templates/new_car.html`

## Troubleshooting

- Pylance Optional comparison warning in `car_manage/forms.py`:
  - Guard against `None` and compare with `Decimal` in `clean_value()`:
    `if value is not None and value < Decimal('10000'):`

- “Attribute get unknown for list[str]”:
  - Ensure you call `.get()` on a dict-like (`request.GET`, `request.POST`, QueryDict, or dict), not a list. Example usage in `views.py`: `search = request.GET.get('search')`.

## Common Commands

- `python manage.py runserver` — start dev server
- `python manage.py makemigrations && python manage.py migrate` — DB changes
- `python manage.py createsuperuser` — admin user
- `python manage.py changepassword <username>` — reset password

## Production Checklist (later)

- Set `DEBUG = False`, configure `ALLOWED_HOSTS`.
- Generate a secure `SECRET_KEY` via environment variable.
- Configure static files and a proper media server.

