from django.db import models

class Car(models.Model):
  
  id = models.AutoField(primary_key=True) #unic ID with auto increment
  model = models.CharField(max_length=200)  #char field 
  brand = models.CharField(max_length= 100) #char field
  factory_year = models.IntegerField(blank=True, null=True) #can skip some info
  model_year = models.IntegerField(blank=True, null=True) #can skip some info
  value = models.FloatField(blank=True, null=True) # float number for the model value and can skip some info
  
