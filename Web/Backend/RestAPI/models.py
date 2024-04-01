from django.db import models

class ModelAPI(models.Model):
    path_video = models.CharField(max_length=100)
    path_model = models.CharField(max_length=100)
    
class ResultAPI(models.Model):
    NumberPeople = models.IntegerField()
    Date = models.DateField()
    