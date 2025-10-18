# Car Manage (WIP)

Short project description
This is a small Django project to manage cars (models, brands, years, value). The main app is `car_manage` and the core model is [`car_manage.models.Car`](car_manage/models.py). The project is still being developed.

Status
- Work in progress — not production ready.
- Initial model and migration created: [car_manage/migrations/0001_initial.py](car_manage/migrations/0001_initial.py).

Directory highlights
- Entry point: [manage.py](manage.py)
- Project settings: [app/settings.py](app/settings.py)
- URL config: [app/urls.py](app/urls.py)
- App: [car_manage](car_manage/)
  - Models: [car_manage/models.py](car_manage/models.py)
  - Views: [car_manage/views.py](car_manage/views.py)
  - Admin: [car_manage/admin.py](car_manage/admin.py)

Quick start (development)
1. Create virtual env and install dependencies:
   python -m venv .venv
   .venv\Scripts\activate   (Windows) or source .venv/bin/activate (mac/linux)
   pip install -r requirements.txt  # or pip install django

2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

3. Create a superuser (optional):
   python manage.py createsuperuser

4. Run development server:
   python manage.py runserver

Notes & next steps
- Add views, templates and API endpoints for CRUD operations in [car_manage/views.py](car_manage/views.py).
- Register `Car` in admin at [car_manage/admin.py](car_manage/admin.py).
- Add tests in [car_manage/tests.py](car_manage/tests.py).
- Consider locking SECRET_KEY and turning DEBUG off for production in [app/settings.py](app/settings.py).

Contact / author
- Project scaffolded via Django. See [manage.py](manage.py) for command usage.