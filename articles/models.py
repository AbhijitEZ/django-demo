from django.db import models
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def truncate_snippet(self):
        return self.body[0:60] + '...'
