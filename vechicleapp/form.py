from django import forms
from .models import Vechicle

class VechicleForm(forms.ModelForm):
    class Meta:
        model=Vechicle
        fields=['name','desc','img']