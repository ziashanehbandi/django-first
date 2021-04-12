from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=60)
    describtion = models.CharField(max_length=200)
    images = models.ImageField(upload_to='image')
    url = models.URLField(blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=60)
    describtion = models.CharField(max_length=400)
    date = models.DateField()

