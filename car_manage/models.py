from django.db import models


class Brand(models.Model):
  
  id = models.AutoField(primary_key= True) #unic ID 
  name = models.CharField(max_length=200) 
  
  def __str__(self):
   return self.name  # must match the same name given or else nothing works 

class Car(models.Model):
  
  id = models.AutoField(primary_key=True) #unic ID with auto increment
  model = models.CharField(max_length=200)  #char field 
  brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name= 'car_brand') # foreignkey to get the brands from the Brand Class || PROTECT to keep the brand safe
  factory_year = models.IntegerField(blank=True, null=True) #can skip some info
  model_year = models.IntegerField(blank=True, null=True) #can skip some info
  value = models.FloatField(blank=True, null=True) # float number for the model value and can skip some info
  
  def __str__(self):
    return self.model #remove the "Car Object()"