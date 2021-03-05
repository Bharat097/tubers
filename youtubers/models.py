from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'Solo'),
        ('small', 'Small'),
        ('large', 'Large'),
    )

    camera_choices = (
        ('canon', 'Canon'),
        ('nikon', 'Nikon'),
        ('sony', 'Sony'),
        ('red', 'Red'),
        ('fuji', 'Fuji'),
        ('panasonic', 'Panasonic'),
        ('other', 'Other')
    )

    category_choices = (
        ('code', 'Code'),
        ('mobile_review', 'Mobile Review'),
        ('vlogs', 'Vlogs'),
        ('comedy', 'Comedy'),
        ('gaming', 'Gaming'),
        ('film_making', 'Film Making'),
        ('cooking', 'Cooking')
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='youtubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.utcnow())
