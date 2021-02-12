from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    enroll = models.IntegerField()

    def __str__(self):
        return self.name[:6]
    