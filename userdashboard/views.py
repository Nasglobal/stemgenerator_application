from django.shortcuts import render
from django.http import JsonResponse
from .models import MediaFiles,SpleetedAudios
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import FilesSerializers,MultipleFileSerializer
from spleeter.separator import Separator
import soundfile as sf 
import json

import os



# Create your views here.

class FileViewset(viewsets.ModelViewSet):
  queryset = MediaFiles.objects.all()
  serializer_class = FilesSerializers


  @action(detail=False, methods=["POST"]) #convert this to endpoint
  def multiple_upload(self, request, *args, **kvargs):
    serializer = MultipleFileSerializer(data=request.data or None)
    serializer.is_valid(raise_exception=True)
    audios = serializer.validated_data.get('audios')

    audio_list = []
    for audio in audios:
      audio_list.append(MediaFiles(audio=audio))

    if audio_list:
      MediaFiles.objects.bulk_create(audio_list)
    return Response("success")





def spleet(request,id):
  audio_id = MediaFiles.objects.get(id=id)
  audio = audio_id.audio
  auI = str(audio_id.id)
  aud = str(audio)
  audio_dir =aud[:-4]
  input_file = f"media/{audio}"
  output_dir = "media/output"
  separator = Separator('spleeter:4stems')
  separator.separate_to_file(input_file,output_dir)
  v = f"{output_dir}/{audio_dir}"
  vocals_file = f"{v}/vocals.wav"
  bass_file = f"{v}/bass.wav"
  piano_file = f"{v}/other.wav"
  drums_file = f"{v}/drums.wav"

  #adding the splitted audios to database
  splitedaudio_list = []
  splitedaudio_list.append(vocals_file)
  splitedaudio_list.append(bass_file)
  splitedaudio_list.append(piano_file)
  splitedaudio_list.append(drums_file)

  
  
  data, samplerate = sf.read(vocals_file)
  sf.write(f"{v}/vocals.mp3",data,samplerate) 

  data, samplerate = sf.read(bass_file)
  sf.write(f"{v}/bass.mp3",data,samplerate) 

  data, samplerate = sf.read(piano_file)
  sf.write(f"{v}/other.mp3",data,samplerate) 

  data, samplerate = sf.read(drums_file)
  sf.write(f"{v}/drums.mp3",data,samplerate)

  for audio in splitedaudio_list:
    os.remove(audio)
  audiosmp3 = []
  audiosmp3.append(f"{v}/vocals.mp3")
  audiosmp3.append(f"{v}/bass.mp3")
  audiosmp3.append(f"{v}/other.mp3")
  audiosmp3.append(f"{v}/drums.mp3")

  

  if audiosmp3:
    for audio in audiosmp3:
      SpleetedAudios(splited_audio=audio,originalAudioId=auI).save()

  
  return JsonResponse({"data":"success"})


def getSpleetedAudios(request,id):

  splited_audios = SpleetedAudios.objects.filter(originalAudioId=id).values()
  return JsonResponse({"data":list(splited_audios)})



def checksplit(request):
  splited_audios = SpleetedAudios.objects.all().values()
  return JsonResponse({"data":list(splited_audios)})


