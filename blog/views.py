from rest_framework import viewsets, permissions
from .models import Blog, Author, Category
from .serializers import (
    BlogSerializer,
    AuthorSerializer,
    CategorySerializer
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Author'])
class AuthorViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



@extend_schema(tags=['Blog'])
class BloglistViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




@extend_schema(tags=['Category']) 
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    

