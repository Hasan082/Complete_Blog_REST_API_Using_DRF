from rest_framework import viewsets, permissions
from .models import Blog, Author, Category
from .serializers import BlogSerializer, AuthorSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema
from .pagination import BlogPagination


@extend_schema(tags=["Author"])
class AuthorViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=["Blog"])
class BloglistViewset(viewsets.ReadOnlyModelViewSet):
    # queryset = Blog.objects.filter(is_published=True) # Using it in get_queryset method
    serializer_class = BlogSerializer
    pagination_class = BlogPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Blog.objects.filter(is_published=True)
        category_slug = self.request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)
        return queryset
        
    


@extend_schema(tags=["Category"])
class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
