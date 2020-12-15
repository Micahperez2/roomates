"""roommates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from house import views as house_views
from assignments import views as assignments_views
from rest_framework import routers


router = routers.DefaultRouter()
#router.register(r'users', house_views.UserViewSet)
#router.register(r'home', house_views.TaskViewSet)
#router.register(r'assignments', assignments_views.assignmentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('house/', house_views.house, name='house'),
    path('join_group/', house_views.join_group, name='join_group'),
    path('make_group/', house_views.make_group, name='make_group'),
    path('assignments/', assignments_views.assignments, name='assignments'),
    path('join/', core_views.join, name='join'),
    path('login/', core_views.user_login, name='user_login'),
    path('logout/', core_views.user_logout, name='user_logout'),
    path('api/v1/', include(router.urls)),
    path('api-auth/v1/', include('rest_framework.urls', namespace='rest_framework'))
]
