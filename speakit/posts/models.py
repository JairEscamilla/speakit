from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post = models.CharField('Post', max_length=150, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post 
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'