from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    tlf = models.CharField(max_length=10)

class Article(models.Model):
    article_name = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    price = models.IntegerField()
    

class Orders (models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
    