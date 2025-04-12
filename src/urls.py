from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('src.apps.authentication.urls')),
    path('rewards/', include('src.apps.rewards.urls')),
]
