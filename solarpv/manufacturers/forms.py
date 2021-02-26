from django import forms
from .models import Manufacturer

class Manufacturerform(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['mName', 'registeredCountry', 'cName']
