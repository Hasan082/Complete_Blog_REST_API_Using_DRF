from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from .models import Blog, Author, Category, Comment
from .serializers import (
    BlogSerializer,
    AuthorSerializer,
    CategorySerializer,
    CommentSerializer
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Author'])
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=['Blog'])
class BloglistViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.select_related('author').prefetch_related('categories').filter(is_published=True)
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



@extend_schema(tags=['Category']) 
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
        
@extend_schema(tags=['Comment'])
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
