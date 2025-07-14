from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

class MovieList(APIView):

    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self, request):
        movies=Movies.objects.all()
        serializer=MoviesMainPageSerializer(movies, many=True)
        return Response(serializer.data)
    
class MovieDetail(APIView):
    
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        movie=get_object_or_404(Movies, pk=pk)
        return movie
    
    def get(self, request, pk):
        movie=self.get_object(pk=pk)
        serializer=MoviesSerializer(movie)
        return Response(serializer.data)
    