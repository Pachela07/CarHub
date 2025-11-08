from typing import Any
from django import forms  #Reusing tools already created on Django
from car_manage.models import Car #*No need to use the foreign key anymore only the class. 
from decimal import Decimal #!Need to use this import cause in my model im using value with DecimalField
#### Making the form but doing everything manually #### !Do not use this anymore 
""" class CarForm(forms.Form):
    model = forms.CharField(
        max_length=40,
        label="Model",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Audi A4"})
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(), #Dont forget to use this cause of the foreign key
        label="Brand",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    plate = forms.CharField(
        max_length=20,
        required=False,
        label="License Plate",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. ABC-1234"})
    )
    factory_year = forms.IntegerField(
        min_value=1900,
        max_value=2100,
        label="Factory Year",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 2021"})
    )
    model_year = forms.IntegerField(
        required=False,
        min_value=1900,
        max_value=2100,
        label="Model Year",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 2022"})
    )
    value = forms.DecimalField(
        max_digits=9,
        decimal_places=0,
        min_value=0,
        label="Price (€)",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 18000"})
    )
    photo = forms.ImageField(
        label="Photo",
        widget=forms.ClearableFileInput(attrs={"class": "form-control", "accept": "image/*"})
    )
    #### NEW METHOD TO SAVE THE FORM #####
    def save(self):
        new_car = Car ( # New Car object with the data from the form
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            plate = self.cleaned_data['plate'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
            
        )
        new_car.save() # Save it in the DB so we can use in the view
        return new_car """

##### SAME THING BUT USING MODELFORM NOW CAUSE IM RTARDED AND DIDNT KNEW THIS :) ######
class CarModelForm(forms.ModelForm): 
    class Meta:
        model = Car ##* Get the Class previously created
        fields = '__all__' ##* Get all the values from the form
        
    ####VALIDATIONS####   
    #! Validations must always use the 'clean_'
    def clean_value(self):
        value = self.cleaned_data.get('value') #? capture the value filled by the user 
        if value != None and value < Decimal('5000'):
            self.add_error('value', 'The mininum value for the cars should be at least 5.000€')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year !=None and factory_year < 1966:
            self.add_error('factory year', "For safety, maintenance and price costs. We dont accept vehicles before the year reported")
            return factory_year