from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class UserProfile(models.Model):  # ONE TO ONE
    # each user Profile has a User
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=1024)
    profile_pic_url = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.bio}'


class Post(models.Model):
    post_user = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'POST: {self.content}'


class Comment(models.Model):
    comment_user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'COMMENT: {self.content}'


class Reply(models.Model):
    reply_user = models.ForeignKey(
        User, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'REPLY: {self.content}'


class Reaction(models.Model):
    type = models.CharField(max_length=16)

    def __str__(self):
        return f'REACTION: {self.type}'


class PostReaction(models.Model):
    reaction = models.ForeignKey(
        Reaction, related_name='post_reactions', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='post_reactions', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='post_reactions', on_delete=models.CASCADE)
