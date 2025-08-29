from django import forms 
# from django.db import models 
from .models import Library


class LibraryForm(forms.ModelForm):
    class Meta:
        model=Library
        fields='__all__'