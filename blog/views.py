from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema

from .models import Blog, Author, Category
from .serializers import BlogSerializer, AuthorSerializer, CategorySerializer
from .pagination import BlogPagination


# ------------------------
# Author ViewSet
# ------------------------
@extend_schema(
    tags=["Author"],
    summary="List or retrieve authors by slug",
    description="Returns all authors or a single author using slug in the URL. SEO-friendly."
)
class AuthorViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'  # Allow /api/authors/<slug>/
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ------------------------
# Blog ViewSet
# ------------------------
@extend_schema(
    tags=["Blog"],
    summary="List and filter published blog posts",
    description=(
        "Read-only view for published blog posts. "
        "Supports filtering by `?category=<slug>` or `?author=<slug>`."
    )
)
class BloglistViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer
    pagination_class = BlogPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):  # type: ignore
        request: Request = self.request  # type: ignore
        queryset = super().get_queryset()

        # Filter by category slug
        category_slug = request.query_params.get('category')
        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)

        # Filter by author slug
        author_slug = request.query_params.get('author')
        if author_slug:
            queryset = queryset.filter(author__slug=author_slug)

        return queryset

    @extend_schema(
        summary="Latest 5 blog posts",
        description="Returns the 5 most recent published blog posts."
    )
    @action(detail=False, methods=['get'], url_path='latest')
    def latest_blogs(self, request):
        latest_posts = Blog.objects.filter(is_published=True)[:5]
        serializer = self.get_serializer(latest_posts, many=True)
        return Response(serializer.data)


# ------------------------
# Category ViewSet
# ------------------------
@extend_schema(
    tags=["Category"],
    summary="List or retrieve blog categories by slug",
    description="Returns all categories or a single category using slug in the URL."
)
class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'  # Allow /api/categories/<slug>/
    
    # Note: `lookup_field = 'slug'` allows using slugs in the URL
    # This is useful for SEO-friendly URLs and better user experience
    # Example: /api/categories/technology/
    # Instead of /api/categories/1/
    # This makes it easier to remember and share category links