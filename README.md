# Car Manage (WIP)

A Django project for managing cars, including models, brands, years, and values.  
**Status:** Work in progress — not production ready.

## Latest Updates (2025-10-22)

- Project scaffold completed.
- Initial `Car` model and migration created.
- Updated routes: `index` view now uses `car_view` in `app/urls.py`.
- `index.html` replaced with new `cars.html` content; improved car listing and UI.
- In `car_manage/views.py`:
  - `car_view` now renders `index.html`.
  - Old `index` function renamed to `skeleton`.
  - Removed usage of `cars.html`.

## Project Structure

.
├── manage.py
├── app/
│ ├── settings.py
│ └── urls.py
└── car_manage/
├── models.py
├── views.py
├── admin.py
├── migrations/
│ └── 0001_initial.py
└── templates/
├── index.html # Main car listing UI
└── cars.html # (No longer in use)

## Quick Start (Windows)

1. **Create and activate a virtual environment:**

   python -m venv .venv
   .venv\Scripts\activate

2. **Install dependencies:**

   pip install -r requirements.txt

   - If `requirements.txt` is missing:

     pip install django

3. **Apply migrations:**

   python manage.py makemigrations
   python manage.py migrate

4. **(Optional) Create a superuser:**

   python manage.py createsuperuser

5. **Run the development server:**

   python manage.py runserver

## Next Steps

- Implement CRUD views, templates, and API endpoints in `car_manage/views.py`.
- Register the `Car` model in the admin interface (`car_manage/admin.py`).
- Add unit tests in `car_manage/tests.py`.
- Move secrets out of source control and set `DEBUG = False` for production in `app/settings.py`.
- Consider adding CI, code linting, and a requirements lock file.

## Contributing

- Use feature branches and open pull requests for new features or fixes.
- Include tests for all new behavior.

## Contact & Help

- Built with Django.
- For available commands, run:

  python manage.py help
