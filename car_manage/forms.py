from django import forms  #Reusing tools already created on Django
from car_manage.models import Brand,Car # needs to be imported to use the foreign key # And Car to use the model

# Same info thats registered in the class
class CarForm(forms.Form):
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
        return new_car