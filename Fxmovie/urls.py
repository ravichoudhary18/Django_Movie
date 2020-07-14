from django.urls import path
from .views import movieList, movieDetail

urlpatterns = [
    path('',movieList.as_view(), name='movie_list'),
    path('<int:pk>/',movieDetail.as_view(), name='movie_detail'),
]
