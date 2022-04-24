from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)# default=ACTIVE)
    date_added = models.DateTimeField(auto_now_add=True)
    protected = models.BooleanField(default=False)
    password = models.CharField(null=True, max_length=40)
    private = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'News'
