from django.db import models

# Create your models here.
class Blogs(models.Model):
    content=models.CharField(max_length=255)
    title=models.CharField(max_length=50)

    def __str__(self):
         return self.title