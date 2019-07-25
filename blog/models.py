from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title
