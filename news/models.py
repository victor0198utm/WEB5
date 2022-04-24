from tkinter import ACTIVE
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, default=ACTIVE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'News'
