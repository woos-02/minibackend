from django.core.management.base import BaseCommand
import requests
from movies.models import *

class Command(BaseCommand):

  def handle(self, *args, **kwargs):
    url = "http://43.200.28.219:1313/movies/"
    res = requests.get(url)
    
    movies = res.json()['movies']
    count=0
    count_actor=0
    
    for movie in movies: 
      m = Movies.objects.create(
        title_kor=movie['title_kor'],
        title_eng=movie['title_eng'],
        poster_url=movie['poster_url'],
        genre=movie['genre'],
        showtime=movie['showtime'],
        release_date=movie['release_date'],
        plot=movie['plot'],
        rating=movie['rating'],
        director_name=movie['director_name'],
        director_image_url=movie['director_image_url'],
        )
      
      for actor_name in movie['actors']:
        actor, _ = Actors.objects.get_or_create(name=actor_name)
        m.actors.add(actor)
        count_actor+=1
        

      count+=1

    self.stdout.write(self.style.SUCCESS(f"{count}개의 영화 데이터와 {count_actor}개의 배우 데이터를 저장했습니다."))
      