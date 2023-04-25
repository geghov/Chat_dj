from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('text')
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return self.text