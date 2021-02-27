from django import forms
from .models import Manufacturer

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['manufacturer', 'modelNumber', 'length', 'width', 'weight',
         'totalnumofCells', 'numberofseriesStrings', 'seriesfuseRating',
         'frameType', 'maxVoltage', 'voc', 'isc', 'vmp', 'imp', 'pmp', 'ff']
