from django import forms
from .models import MYFILEUPLOAD

class MYFILEFORM(forms.ModelForm):
    
    class Meta:
        model = MYFILEUPLOAD
        fields = '__all__'