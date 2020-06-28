from django.db import models

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

    def __str__(self):
        return self.title