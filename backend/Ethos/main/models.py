from django.db import models
from email.policy import default
from django.contrib.auth.models import User

class Audio(models.Model):
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uploader')
    audioFile = models.FileField(upload_to="audio_uploads/audio/")
    def __str__(self):
        return str(self.uploaded_by)

class TimeStamp(models.Model):
    audio = models.ForeignKey(Audio,on_delete=models.CASCADE,related_name="audio")
    comment = models.TextField(max_length=500)
    time = models.TimeField()
    def __str__(self):
        return str(self.time,self.audio)
class upload(models.Model):
    video=models.FileField(upload_to="main/media/")