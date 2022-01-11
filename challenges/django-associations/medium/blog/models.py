from django.db import models


class User(models.Model):
    pass


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts',
                               on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
