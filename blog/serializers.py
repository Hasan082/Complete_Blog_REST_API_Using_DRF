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
        
        
class AuthorCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'profile_picture']
        read_only_fields = ['id']


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
    author = AuthorCompactSerializer(read_only=True)
      
    categories = CategorySerializer(many=True, read_only=True)
    
    category_ids = serializers.PrimaryKeyRelatedField(
        source='categories', queryset=Category.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'blog_img', 'author',
            'categories', 'category_ids',
            'created_at', 'updated_at', 'is_published'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

