from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    create_time = models.TimeField(null=True)
    
    def __str__(self):
        return self.title
