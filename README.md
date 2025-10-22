# Car Manage (WIP)

Short description
This is a small Django project to manage cars (models, brands, years, value). The main app is `car_manage`. The project is under active development.

Latest updates (2025-10-22)

- Project scaffold completed.
- Initial `Car` model and migration created.
- README updated with quick-start instructions and next steps.

Status

- Work in progress — not production ready.
- Tests and full CRUD views/templates/API are not implemented yet.

Key files

- Entry point: `manage.py`
- Project settings: `app/settings.py`
- URL config: `app/urls.py`
- App: `car_manage/`
  - Models: `car_manage/models.py`
  - Admin: `car_manage/admin.py`
  - Migrations: `car_manage/migrations/0001_initial.py`

Quick start (Windows)

1. Create and activate virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt
   (or `pip install django` if requirements.txt is missing)

3. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

4. (Optional) Create superuser:
   python manage.py createsuperuser

5. Run development server:
   python manage.py runserver

Notes and next steps

- Add views, templates, and API endpoints for CRUD operations in `car_manage/views.py`.
- Register `Car` in admin (`car_manage/admin.py`) if not already registered.
- Add unit tests in `car_manage/tests.py`.
- Move secrets out of source control and set DEBUG = False for production in `app/settings.py`.
- Consider adding CI, linting, and a requirements lock file.

Contributing

- Create feature branches, open PRs, and include tests for new behavior.

Contact / author

- Project scaffolded with Django. Use `python manage.py help` for available commands.
