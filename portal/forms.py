from django import forms
from .models import MyFileUpload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyFileForm(forms.ModelForm):
    
    class Meta:
        model = MyFileUpload
        fields = '__all__'
        

class SignUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields =['username','password1','password2']        
