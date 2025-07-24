from rest_framework import serializers
from .models import Author, Blog, Category
from django.contrib.auth import get_user_model

User = get_user_model()

# -------------------------------
# Author Serializer
# -------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'user', 'full_name', 'bio', 'profile_picture']
        read_only_fields = ['id', 'user']

# -------------------------------
# Category Serializer
# -------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id', 'slug']

# -------------------------------
# Blog Serializer
# -------------------------------
class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author', queryset=Author.objects.all(), write_only=True, required=False
    )
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        source='categories', queryset=Category.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'author_id',
            'categories', 'category_ids',
            'created_at', 'updated_at', 'is_published'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

