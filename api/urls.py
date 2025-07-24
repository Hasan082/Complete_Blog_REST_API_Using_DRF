from django.urls import path
from rest_framework import routers
from blog.views import (
    BloglistViewset,
    AuthorViewset,
    CategoryViewset
)

routers = routers.DefaultRouter()
routers.register(r'authors', AuthorViewset)
routers.register(r'blogs', BloglistViewset)
routers.register(r'categories', CategoryViewset)



urlpatterns = [] + routers.urls
