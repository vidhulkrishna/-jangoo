from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=400)
    Age=models.IntegerField()
    Dob=models.DateField()
    Address=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='student_image/')
