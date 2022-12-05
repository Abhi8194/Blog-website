from dataclasses import fields
from pyexpat import model
from .models import blog
from django import forms
from django.forms.widgets import TextInput

class django_form(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'

        widgets = {
            'Upload_by' : TextInput(attrs= {'id':'username','type':'hidden'})
        }