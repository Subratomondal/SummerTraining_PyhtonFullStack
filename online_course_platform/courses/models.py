from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
