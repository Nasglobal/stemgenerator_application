from rest_framework import serializers
from .models import MediaFiles,SpleetedAudios


class FilesSerializers(serializers.ModelSerializer):
  class Meta:
    model = MediaFiles
    fields = ['id','audio']

class MultipleFileSerializer(serializers.Serializer):
  audios = serializers.ListField(
    child = serializers.FileField()
  )





