from django.urls import path
from rest_framework import routers
from myaccount.views import UserViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)


urlpatterns = [] + routers.urls

