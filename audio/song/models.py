from django.db import models

# Create your models here.
class Song(models.Model):
    sname = models.CharField(max_length=100)
    duration = models.DateTimeField()
    uploadfile = models.FileField(upload_to = 'ps2')
    uploadtime = models.TimeField('', auto_now_add=False)

