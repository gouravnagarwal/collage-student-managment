from django.db import models

# Create your models here.

class Student(models.Model):
    def __str__(self):
        return self.name
    rollno=models.IntegerField()
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    percentage=models.IntegerField()