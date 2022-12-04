from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Rating(models.Model):
    RATE_CHOICES = (
        (4, "excellent"),
        (3, "very good"),
        (2, "good"),
        (1, "bad"),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, related_name='ratings', on_delete=models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'