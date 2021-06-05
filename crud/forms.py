from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('name','email','age')
        widgets = {
            'name':forms.TextInput(attrs={'id':'nameId'}),
            'email':forms.EmailInput(attrs={'id':'emailId'}),
            'age':forms.NumberInput(attrs={'id':'ageId'}),
        }