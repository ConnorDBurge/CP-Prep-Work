from django.db import models


class Post(models.Model):
    post_text = models.TextField(null=True)

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    comment_text = models.TextField(null=True)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text
