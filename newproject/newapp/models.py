from distutils.command.upload import upload
from django.db import models

# Create your models here.
class blog(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    Img=models.ImageField(upload_to='image')
    Upload_by=models.CharField(max_length=100,null=True)
