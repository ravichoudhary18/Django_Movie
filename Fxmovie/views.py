from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Movie

class movieList(ListView):
    model = Movie
    paginate_by = 1
    # context_object_name = ''
    # template_name=''

class movieDetail(DetailView):
    model = Movie
    # template_name=''