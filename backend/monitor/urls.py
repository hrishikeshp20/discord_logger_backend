from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('discord-health/', views.discord_health_check, name='discord_health_check'),
]
