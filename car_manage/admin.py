from django.contrib import admin
from car_manage.models import Car, Brand
class CarAdmin(admin.ModelAdmin): #admin based class
  list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #values that match my db
  search_fields = ('model', 'brand') #search field by model #DONT FORGET THE ","
  
class BrandAdmin(admin.ModelAdmin):
  list_display = ('name',) # value that match my db
  search_fields = ('name',) #search field by name 
  

admin.site.register(Brand, BrandAdmin)  # Loads the import from Brand class 
admin.site.register(Car, CarAdmin) # loads the import from Car class 
