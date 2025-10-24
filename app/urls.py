# Provide Django admin site (needed to include admin URLs)
from django.contrib import admin
# path() to define URL patterns
from django.urls import path
# Access project settings (e.g. MEDIA_URL / MEDIA_ROOT)
from django.conf import settings
# Helper to serve static/media files during development
from django.conf.urls.static import static
from car_manage.views import car_view # import from the view file
#from car_manage.views import index 



############### ADM & USER VIEW - URLS ###################

urlpatterns = [
    path('admin/', admin.site.urls), #Admin page
    path('index/', car_view), #Car view 
   # path('index/', index), # Default page skeleton
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # Admin route and media content 

