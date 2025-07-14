from rest_framework import serializer
from .models import *

class ActorsSerializer(serializer.ModelSerializer):
  class Meta:
    model=Actors
    fields = ['name', 'character', 'image_url']

class MoviesSerializer(serializer.ModelSerialzer):
  class Meta:
    model=Movies
    fields= '__all__' 

class CommentsSerializer(serializer.ModelSerializer):
  class Meta:
    model=Comments
    fields=['username', 'content', 'create_date']