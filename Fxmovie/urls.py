from django.urls import path
from .views import movieList, movieDetail

urlpatterns = [
    path('',movieList.as_view(), name='movie_list'),
    path('<slug:slug>',movieDetail.as_view(), name='movie_detail'),
]
