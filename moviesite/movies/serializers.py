from rest_framework import serializers
from .models import *

class ActorsSerializer(serializers.ModelSerializer):
  class Meta:
    model=Actors
    fields = ['name', 'character', 'image_url']

class MoviesSerializer(serializers.ModelSerializer):
  actors = ActorsSerializer(many=True)
  
  class Meta:
    model=Movies
    fields= '__all__' 

class CommentsSerializer(serializers.ModelSerializer):
  username=serializers.StringRelatedField(read_only=True)
  
  class Meta:
    model=Comments
    fields=['username', 'content', 'create_date']

from rest_framework import serializers
from .models import Movies, Comments
