"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def api_base_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({"api_base_url": base_url})

def activities_endpoint(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    url = f"https://{codespace_name}-8000.app.github.dev/api/activities/"
    return JsonResponse({"endpoint": url})

def teams_endpoint(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    url = f"https://{codespace_name}-8000.app.github.dev/api/teams/"
    return JsonResponse({"endpoint": url})

def users_endpoint(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    url = f"https://{codespace_name}-8000.app.github.dev/api/users/"
    return JsonResponse({"endpoint": url})

def workouts_endpoint(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    url = f"https://{codespace_name}-8000.app.github.dev/api/workouts/"
    return JsonResponse({"endpoint": url})

def leaderboard_endpoint(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    url = f"https://{codespace_name}-8000.app.github.dev/api/leaderboard/"
    return JsonResponse({"endpoint": url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_base_url),
    path('api/activities/', activities_endpoint),
    path('api/teams/', teams_endpoint),
    path('api/users/', users_endpoint),
    path('api/workouts/', workouts_endpoint),
    path('api/leaderboard/', leaderboard_endpoint),
]
