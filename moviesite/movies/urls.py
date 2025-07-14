from django.urls import path
from . import views

app_name='movies'

urlpatterns=[
    path('', views.movie_list,  name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/comments/', views.add_comment, name='add_comment'),
]