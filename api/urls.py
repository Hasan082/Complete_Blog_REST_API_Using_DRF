from django.urls import path
from rest_framework import routers
from blog.views import (
    BloglistViewset,
    AuthorViewset,
    CategoryViewset
)

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewset, basename='author')
router.register(r'blogs', BloglistViewset, basename='blog')
router.register(r'categories', CategoryViewset, basename='category')



urlpatterns = [] + router.urls
