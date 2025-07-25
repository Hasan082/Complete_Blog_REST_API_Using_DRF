from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    full_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="authors", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        if Author.objects.filter(slug=self.slug).exists() and not self.pk:
            raise ValueError(f"Author with slug '{self.slug}' already exists.")
        if not self.user:
            raise ValueError("Author must have a user associated with it.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        if Category.objects.filter(slug=self.slug).exists() and not self.pk:
            raise ValueError(f"Category with slug '{self.slug}' already exists.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200, unique=True)
    blog_img = models.ImageField(upload_to="blogs", blank=True, null=True)
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
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if Blog.objects.filter(slug=self.slug).exists() and not self.pk:
            raise ValueError(f"Blog with slug '{self.slug}' already exists.")
        if not self.author:
            raise ValueError("Blog must have an author.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


