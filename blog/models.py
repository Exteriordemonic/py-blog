from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="coments"
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="coments"
    )

    def __str__(self) -> str:
        return self.content
