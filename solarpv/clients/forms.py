from django import forms
from .models import Client

class Clientform(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'passwd', 'fName', 'mName', 'lName',
        'address', 'city', 'state', 'zipCode',
        'officePhone', 'cellPhone', 'email']
