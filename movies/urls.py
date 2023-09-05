from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/movies/3
# http://127.0.0.1:8000/movies/walking-dead

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("movies", views.movies, name="movies"),
    path("movies/<int:id>", views.moviedetails, name="details"),
]