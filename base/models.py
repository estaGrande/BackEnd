from turtle import update
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#se tiene que hacer min 5 modelos *** "py .\manage.py makemigrations" y despues "py .\manage.py migrate" para crear archivo sql


class Post(models.Model):    
    title = models.CharField(max_length=200)
    text = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Baqueros(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class Caballos(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class FloraFauna(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    tipo= models.CharField(max_length=100)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
