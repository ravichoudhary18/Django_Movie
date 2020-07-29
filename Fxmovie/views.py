from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Movie, links

class movieList(ListView):
    model = Movie
    paginate_by = 1
    # context_object_name = ''
    # template_name=''

class movieDetail(DetailView):
    model = Movie
    # template_name=''

    def get_object(self):
        object = super(movieDetail, self).get_object()
        object.views_count = object.views_count +1 
        object.save()
        return object
    
    def get_context_data(self,**kwargs):
        context = super(movieDetail,self).get_context_data(**kwargs)
        context['linkss'] = links.objects.filter(movie = self.get_object())
        return context