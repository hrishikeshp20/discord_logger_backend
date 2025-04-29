from django.contrib import admin
from .models import DiscordUser

@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_name", "join_count", "status") 
    search_fields = ("user_name", "user_id")                         
    list_filter = ("status",)                                      
