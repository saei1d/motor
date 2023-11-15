from django.db import models


# Create your models here.


class Motor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(default='honda.png')
    price = models.BigIntegerField()





class Group_lavazem (models.Model):
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(default="honda.png")




class Lavazem(models.Model):
    lavazem = models.ForeignKey(Group_lavazem, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    color = models.CharField(max_length=255)
    price = models.BigIntegerField()
