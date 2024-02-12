from django.db import models
from django.shortcuts import reverse
from accounts.models import CustomUser


class BlogGroup(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_list')



class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    group = models.ForeignKey(BlogGroup, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='picture', null=True, blank=True)
    file = models.FileField(upload_to='attach', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edit = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
