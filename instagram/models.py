from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    image = models.FileField(upload_to='image')
    description = models.TextField()
    like = models.ManyToManyField(User,default=0, blank=True, related_name='post_like')
    follow = models.ManyToManyField(User, default=0, blank=True, related_name='post_follow')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.FileField(upload_to='profile_pix')
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    website = models.URLField(blank=True, null=True)
    number = models.IntegerField(max_length=20)

    def __str__(self):
        return self.username
