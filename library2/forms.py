from django import forms
from . models import Book

class BookForm(forms.ModelForm): 
    published_date=forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date'}
        ),
        input_formats=['%Y-%m-%d'],
        error_messages={
            'invalid':'enter date format in DD-MM-YYYY'
        }
    )
    class Meta:
        model=Book
        fields='__all__'