from django.db import models


class City(models.Model):
    name = models.TextField()
    sort = models.IntegerField()


class Question(models.Model):
    question = models.TextField()
    score = models.IntegerField()
    city = models.ForeignKey(City)
    created_at = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField()
