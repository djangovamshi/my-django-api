from django.db import models

# Create your models her

class StudentResult(models.Model):
    roll_number=models.IntegerField()
    name=models.CharField(max_length=200)

    dob=models.DateField(max_length=50)
    marks=models.IntegerField()
