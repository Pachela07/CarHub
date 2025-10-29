from django import forms  #Reusing tools already created on Django
from car_manage.models import Brand # needs to be imported to use the foreign key

# Same info thats registered in the class
class CarForm(forms.Form):
    model = forms.CharField(
        max_length=40,
        label="Model",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Audi A4"})
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
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