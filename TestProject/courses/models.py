from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)  # e.g., "4 weeks", "10 hours"

    def __str__(self):
        return self.title