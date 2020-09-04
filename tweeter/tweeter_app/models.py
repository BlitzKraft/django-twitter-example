from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(User):
    email_verified = models.BooleanField(default=False, null=False)
    verified_user = models.BooleanField(default=False, null=False)
    user_currently = models.TextField(max_length=40,  null=False, blank=False)


class MyTweet(models.Model):
    tweet = models.TextField(max_length=250, blank=False, null=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=0)

