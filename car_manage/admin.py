from django.contrib import admin
from car_manage.models import Car
class CarAdmin(admin.ModelAdmin): #admin based class
  list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #values that match my db
  search_fields = ('model', 'brand') #search field by model #DONT FORGET THE ","
  
admin.site.register(Car, CarAdmin) # loads the import from Car class and the model created now
