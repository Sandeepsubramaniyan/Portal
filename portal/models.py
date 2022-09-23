from pickle import FALSE
from django.db import models


class MyFileUpload(models.Model):
    username = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents')    
            
    def __str__(self):
        return self.file_name