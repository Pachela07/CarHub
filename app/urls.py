# Provide Django admin site (needed to include admin URLs)
from django.contrib import admin
# path() to define URL patterns
from django.urls import path
# Access project settings (e.g. MEDIA_URL / MEDIA_ROOT)
from django.conf import settings
# Helper to serve static/media files during development
from django.conf.urls.static import static
from car_manage import views as car_views  # import views module with alias for clarity and maintainability




############### ADM & USER VIEW - URLS ###################

urlpatterns = [
    path('admin/', admin.site.urls), #Admin page
    path('index/', car_views.car_view, name='index'),  # Car view with explicit URL name for reverse() lookups
    #path('new_car/', car_views.new_car_view, name='new_car'),  #Not using ATM
    path('new_car/', car_views.add_new_car, name='new_car'),  # # New Car view, form to add a new car to the page
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # Admin route and media content 

