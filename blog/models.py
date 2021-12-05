from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Blog model
    """
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(
        User, related_name='like', blank=True, default=None)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comment model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return 'Comment on {} by {}'.format(self.post, self.user)
