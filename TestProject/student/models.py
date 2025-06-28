from django.db import models

# Create your models here.
class student(models.Model):
    roll_number = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    def __str__(self):                #getter
        return self.name
