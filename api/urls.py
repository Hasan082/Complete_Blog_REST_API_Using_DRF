from django.urls import path
from rest_framework import routers
from blog.views import BloglistViewset

routers = routers.DefaultRouter()
routers.register(r'blogs', BloglistViewset)


urlpatterns = [] + routers.urls
