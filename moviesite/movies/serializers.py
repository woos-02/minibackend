from rest_framework import serializers
from .models import *

class ActorsSerializer(serializers.ModelSerializer):
  class Meta:
    model=Actors
    fields = ['name', 'character', 'image_url']

class CommentsSerializer(serializers.ModelSerializer):
  username=serializers.PrimaryKeyRelatedField(source='user.username', read_only=True)
  
  class Meta:
    model=Comments
    fields=['id','movie','user','username', 'content', 'create_date']
    read_only_fields = ['user','username', 'create_date']

class MoviesSerializer(serializers.ModelSerializer):
  actors = ActorsSerializer(many=True, read_only = True)
  comments = CommentsSerializer(many=True, read_only=True)
  
  class Meta:
    model=Movies
    fields= '__all__' 

class MoviesMainPageSerializer(serializers.ModelSerializer):
  class Meta:
    model=Movies
    fields=['title_kor','title_eng', 'poster_url']