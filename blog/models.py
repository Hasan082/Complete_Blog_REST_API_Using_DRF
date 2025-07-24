from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from .utils.file_uploads import profile_image_upload_to, blog_image_upload_to

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    full_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=profile_image_upload_to, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.pk or Author.objects.get(pk=self.pk).full_name != self.full_name:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs): 
        if not self.pk or Category.objects.get(pk=self.pk).name != self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200, unique=True)
    blog_img = models.ImageField(upload_to=blog_image_upload_to("blogs"), blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name='blogs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def save(self, *args, **kwargs):
        if not self.pk or Blog.objects.get(pk=self.pk).title != self.title:
            self.slug = slugify(self.title)
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.author:
            raise ValueError("Author must be set before saving a blog post.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


