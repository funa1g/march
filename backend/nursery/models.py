from django.db import models


class City(models.Model):
    name = models.TextField()
    sort = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    city = models.ForeignKey(City)
    text = models.TextField()
    sort = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    text = models.TextField()
    score = models.IntegerField(null=True)
    category = models.ForeignKey(Category, null=True)
    parent = models.ForeignKey('self', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField()
