from django.db import models
from django.utils import timezone

class PingLog(models.Model):
    SOURCE_CHOICES = [
        ('uptime_robot', 'Uptime Robot'),
        ('discord_bot', 'Discord Bot'),
    ]

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.source} at {self.timestamp}"
