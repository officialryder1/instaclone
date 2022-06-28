from django.db import models
from django.contrib.models import User

class Post(models.Model):
    user = Foreignkey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    description = models.TextField()
    like = models.ManyToManyField(User,default=0, blank=True, related_name='post_like')
    follow = models.ManyToManyField(User, dafault=0, blank=True, related_name='post_follow')

    def __str__(self):
        return self.user
