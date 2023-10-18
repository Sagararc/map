from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'



class Form(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'