from django import forms
from .models import *

class CityForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={
          'class' : 'input',
          'placeholder' : 'City Name'
          }))


  class Meta:
    model = City
    fields = '__all__'