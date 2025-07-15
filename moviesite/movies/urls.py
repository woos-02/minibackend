from django.urls import path
from .views import *

app_name='movies'

urlpatterns=[
  path('', MovieList.as_view(), name='movie_list'),
  path('<int:pk>', MovieDetail.as_view(), name='move_detail'),
  path('comments/<int:movie_id>', CommentList.as_view(), name='comment_list_create'),
]