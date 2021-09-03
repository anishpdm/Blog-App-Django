from django.db import models


class Users(models.Model):
    name=models.CharField(max_length=40,default='',blank=True)
    username=models.CharField(max_length=40,default='',blank=True)
    password = models.CharField(max_length=40, default='', blank=True)


class Blogs(models.Model):
    userid = models.IntegerField()
    message=models.CharField(max_length=400,default='',blank=True)
