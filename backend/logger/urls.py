from django.contrib import admin
from django.urls import path, include  # 👈 include is the key

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('database.urls')),  # 👈 includes all routes from logger/urls.py
]
