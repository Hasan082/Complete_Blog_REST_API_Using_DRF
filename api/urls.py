from django.urls import path
from rest_framework import routers
from blog.views import (
    BloglistViewset,
    AuthorViewset,
    CategoryViewset,
    CommentViewset
)

routers = routers.DefaultRouter()
routers.register(r'authors', AuthorViewset)
routers.register(r'blogs', BloglistViewset)
routers.register(r'categories', CategoryViewset)
routers.register(r'comments', CommentViewset)


urlpatterns = [] + routers.urls
