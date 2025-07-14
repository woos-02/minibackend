from rest_framework import serializers
from .models import *

class ActorsSerializer(serializers.ModelSerializer):
  class Meta:
    model=Actors
    fields = ['name', 'character', 'image_url']

class CommentsSerializer(serializers.ModelSerializer):
  username=serializers.StringRelatedField(source='user.username', read_only=True)
  
  class Meta:
    model=Comments
    fields=['id','username', 'content', 'create_date']

class MoviesSerializer(serializers.ModelSerializer):
  actors = ActorsSerializer(many=True)
  Comments = CommentsSerializer(many=True, read_only=True)
  
  class Meta:
    model=Movies
    fields= '__all__' 

