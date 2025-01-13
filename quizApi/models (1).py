from django.db import models

# Create your models here.
#class Question(models.Model):
 #   question = models.CharField(max_length=250)
  #  category = models.CharField(max_length=30)
  #  difficulty = models.CharField(max_length=10)
  #  points = models.IntegerField()
  #  optString = models.CharField(max_length=350)
  #  correctOption = models.IntegerField()

   # def __str__(self):
  #      return self.question

class Pregunta(models.Model):
    question = models.CharField(max_length=250)
    category = models.CharField(max_length=30)
    difficulty = models.CharField(max_length=10)
    optString = models.CharField(max_length=350)
    correctOption = models.IntegerField()

    def __str__(self):
        return self.question