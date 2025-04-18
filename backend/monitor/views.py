from django.http import JsonResponse
from .models import PingLog
import requests

def health_check(request):
    # Log the ping from UptimeRobot
    PingLog.objects.create(source='uptime_robot', message='Ping from UptimeRobot')

    # Ping the Discord bot
    try:
        discord_url = 'https://discord-logger-bot-r6u0.onrender.com'
        payload = {'status': 'ok', 'from': 'django'}
        requests.post(discord_url, json=payload, timeout=3)
    except Exception as e:
        print("Failed to notify Discord:", e)

    return JsonResponse({'status': 'ok'})

@require_POST
@csrf_exempt
def discord_health_check(request):
    # Log the ping from the Discord bot
    print("📥 Received ping from Discord bot")  # For debugging
    PingLog.objects.create(source='discord_bot', message='Ping back from Discord bot')
    return JsonResponse({'status': 'ok'})
