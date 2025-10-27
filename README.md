# Car Manage (WIP)

A Django project for managing cars, including models, brands, years, and values.  
**Status:** Work in progress — not production ready.

## Latest Updates (2025-10-27)

- Introduced base template [skeleton.html](app/templates/skeleton.html) with:
  - Navbar wired to `{% url 'index' %}` and `{% url 'new_car' %}`, search box using GET param `search`.
  - Shared hero with blocks `hero_title` and `hero_subtitle`, site footer, Bootstrap, and static CSS.
  - Safe JS helpers for card filtering, modal population, and contact form.
- Refactored pages to extend the base:
  - [index.html](car_manage/templates/index.html) extends the base and contains only page sections (features, inventory grid, contact form, details modal).
  - [new_car.html](car_manage/templates/new_car.html) extends the base, sets custom hero text, and includes the add-car form.
- Fixed template errors by:
  - Adding `{% block hero %}` around the hero section and ensuring proper `{% endblock %}` placement in the base.
  - Normalizing block tags in `new_car.html` to avoid “Invalid block tag” and “Unclosed tag” errors.
- No database or URL name changes; existing names `index` and `new_car` remain. The search GET param is `search` and is consumed in [car_view()](car_manage/views.py:6).

## Project Structure

.
├── manage.py
├── app/
│ ├── settings.py
│ ├── urls.py
│ └── templates/
│ └── skeleton.html # Base template
└── car_manage/
├── models.py
├── views.py
├── admin.py
├── migrations/
└── templates/
├── index.html # Extends skeleton.html
└── new_car.html # Extends skeleton.html

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
