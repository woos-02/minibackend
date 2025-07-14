from django.db import models

class Actors(models.Model):
  name=models.CharField(max_length=10)
  character=models.CharField(max_length=10)
  image_url=models.TextField()

class Movies(models.Model):
  title_kor=models.CharField(max_length=200)
  title_eng=models.CharField(max_length=200)
  poster_url=models.TextField()
  genre=models.CharField(max_length=100)
  showtime=models.CharField(max_length=10)
  release_date=models.CharField(max_length=10)
  plot=models.TextField()
  rating=models.CharField(max_length=10)
  director_name=models.CharField(max_length=10)
  actors=models.ForeignKey(Actors, on_delete=models.CASCADE)


