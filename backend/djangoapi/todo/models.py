from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255)
    author = models.CharField(max_length=50)

    def __str__(self):
        return 'title {} by {}'.format(self.title, self.author)
