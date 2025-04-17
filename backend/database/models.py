# models.py
from django.db import models

class DiscordUser(models.Model):
    user_id = models.CharField(max_length=30, unique=True)
    user_name = models.CharField(max_length=100)
    join_count = models.IntegerField(default=0)
    status = models.BooleanField(default=True)  # True = in server, False = left


    def __str__(self):
        return f"{self.user_name} ({self.user_id})"
