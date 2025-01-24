from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title
