from django.db import models
from django.utils import timezone

class MyFileUpload(models.Model):
    username = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(blank=True, null=True)
    file_name = models.CharField(max_length=50)
    file_type = models.FileField(upload_to='documents')
    
    def upload(self):
        self.uploaded_at = timezone.now()
        self.save()
        
    def __str__(self):
        self.username