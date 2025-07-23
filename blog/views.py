from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from drf_spectacular.utils import extend_schema
# Create your views here.


@extend_schema(tags=['Blog'])
class BloglistViewset(viewsets.ModelViewSet): 
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer