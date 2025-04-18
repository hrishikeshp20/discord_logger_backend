from django.db import models
from django.utils import timezone
import pytz

class PingLog(models.Model):
    SOURCE_CHOICES = [
        ('uptime_robot', 'Uptime Robot'),
        ('discord_bot', 'Discord Bot'),
    ]

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    timestamp = models.DateTimeField()
    message = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Set timestamp to IST manually
        ist = pytz.timezone('Asia/Kolkata')
        self.timestamp = timezone.now().astimezone(ist)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.source} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
