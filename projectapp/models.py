from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(uplaod_to='project')
    created_at = models.DateTimeField(auto_not_add=True)
