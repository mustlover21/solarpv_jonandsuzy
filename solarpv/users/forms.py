from django import forms
from .models import User

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'passwd', 'conpasswd', 'fName', 'mName', 'lName',
        'gender', 'address', 'city', 'state', 'zipCode',
        'email', 'cellPhone', 'company']
