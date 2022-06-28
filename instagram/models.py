from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    image = models.FileField(upload_to='image')
    description = models.TextField()
    like = models.ManyToManyField(User,default=0, blank=True, related_name='post_like')
    follow = models.ManyToManyField(User, default=0, blank=True, related_name='post_follow')

    def __str__(self):
        return str(self.user)
