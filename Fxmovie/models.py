from django.db import models
from django.utils.text import slugify

# Create your models here.
CATEGORY_CHOICES = [
    ('action','Action'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE'),
]

LANGUAGE_CHOICES = [
    ('english',"ENGLISH"),
    ('hindi',"HINDI"),
]

STATUS_CHOICES = [
    ('RA','RECRNTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
]


class Movie(models.Model):

    title               = models.CharField(max_length =  100)
    description         = models.TextField()   
    image               = models.ImageField(upload_to ='movies')
    category            = models.CharField(max_length = 7, choices = CATEGORY_CHOICES, default = '1')
    language            = models.CharField(max_length = 7, choices = LANGUAGE_CHOICES, default = '1')
    status              = models.CharField(max_length = 2, choices = STATUS_CHOICES, default = '1')
    cast                = models.CharField(max_length =100)
    tag                 = models.CharField(max_length =100)
    year_of_production  = models.DateField()
    views_count         = models.IntegerField(default=0)
    Timestamp           = models.DateTimeField(auto_now_add=True)
    Updated             = models.DateTimeField(auto_now=True)
    slug                = models.SlugField(blank = True, null =True)
    trailer             = models.URLField(blank = True, null =True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs) # Call the real save() method

    def increase(self):
        self.views_count += 1
        self.save()

LINK_CHOICES = [
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK'),

]

class links(models.Model):
    movie = models.ForeignKey(Movie,related_name='movie_wach1_link',on_delete=models.CASCADE,blank = True, null =True)
    type  = models.CharField(max_length=1, choices = LINK_CHOICES,blank = True, null =True)
    link  = models.URLField(blank = True, null =True)

    def __str__(self):
        return '{}' .format(self.movie)