from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):

    comment = models.CharField(max_length=150, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


