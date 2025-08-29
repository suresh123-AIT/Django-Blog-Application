from django import forms
from django.core import validators
from .models import Teacher

class TeachersForm(forms.ModelForm):
    name=forms.CharField(validators=[validators.MaxLengthValidator(10)],
                         widget=forms.TextInput(attrs={'class':'form-control'}),label='Your Name')
    class Meta:
        model=Teacher
        fields='__all__'
        labels={
            'name':'your name',
            'email':'your Email',
            'phone_number':'contact number',
            'bio':'Your details'
        }
        widgets={
            # 'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'})
        }

        help_texts={
            'name':'name length should be 10 charecters',
            'email':'we accept only gmails',
        }
        error_messages={
            'name':{
                'id_name':'name field should not be empty'
            }
        }








#     name=forms.CharField(min_length=5,label='Your Name',label_suffix='',error_messages={'min_length':'your name should be more than 5 charecters'},
#                          widget=forms.TextInput(attrs={'class':'form-control'}))
#     email=forms.EmailField(required=False,label='Your Email',label_suffix=''
#                            ,help_text='we only accept emails from gmail.com',widget=forms.EmailInput(attrs={'class':'form-control'}))
#     phone_number=forms.IntegerField(label='contact Number',label_suffix='',help_text='Enter 10 digit mobile number',widget=forms.NumberInput(attrs={'class':'form-control'}))
    
#     Bio=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols':20})) 

# def clean(self):
#     cleaned_data = super().clean()
#     name = cleaned_data.get('name')
#     email = cleaned_data.get('email')
    
#     errors = {}
    
#     if name and name[0].lower() != 's':
#         errors['name'] = 'First letter of name should be S'
    
#     if email and email[0].lower() != 's':
#         errors['email'] = 'First letter of email should be S'
    
#     if errors:
#         raise forms.ValidationError(errors)
    
#     return cleaned_data