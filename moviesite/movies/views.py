from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


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
        self.check_object_permissions(self.request, movie) # 커스텀 permission 부여
        return movie
    
    def get(self, request, pk):
        movie=self.get_object(pk=pk)
        serializer=MoviesSerializer(movie)
        return Response(serializer.data)
    
class CommentList(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]       

    def get_object(self, movie_id):
        movie=get_object_or_404(Movies, id=movie_id)
        self.check_object_permissions(self.request, movie) # 커스텀 permission 부여
        return movie
    
    def get(self,request, movie_id):
        movie=self.get_object(movie_id)
        comments = movie.comments.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)
 
    def post(self,request, movie_id):
        movie=self.get_object(movie_id)

        serializer=CommentsSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(movie = movie, user=request.user)
            return Response(CommentsSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)