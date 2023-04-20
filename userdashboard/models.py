from django.db import models

# Create your models here.


class MediaFiles(models.Model):
  audio = models.FileField(upload_to = '')


  def __str__(self):
    return self.audio

class SpleetedAudios(models.Model):
  splited_audio = models.CharField(max_length = 255)
  originalAudioId = models.CharField(max_length = 255)


  def __str__(self):
    return self.splited_audio