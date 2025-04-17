from django.urls import path
from . import views

urlpatterns = [
    path('sync-user/', views.sync_discord_user),
    path('bulk-sync/', views.bulk_sync_users),
    # Add more routes here
]
