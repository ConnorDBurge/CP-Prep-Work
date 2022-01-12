from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)

    def __str__(self):
        return f'Title: {self.title}, Body: {self.body}'


class Comment(models.Model):
    body = models.TextField(null=False)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Body: {self.body}'
