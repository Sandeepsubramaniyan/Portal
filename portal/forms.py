from django import forms
from .models import MyFileUpload

class MyFileForm(forms.ModelForm):
    
    class Meta:
        model = MyFileUpload
        fields = '__all__'