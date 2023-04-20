from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FileViewset, spleet, getSpleetedAudios,checksplit


router = DefaultRouter()
router.register('audios', FileViewset, basename = 'audios')

urlpatterns = [
    path('api/', include(router.urls)),
    path('split/<str:id>', spleet, name='spleet'),
    path('splited-audios/<str:id>', getSpleetedAudios, name='getSpleetedAudios'),
    path('checksplitted', checksplit, name='checksplit')

]
