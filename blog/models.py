from django.db import models


class Author(models.Model):
    """
    Represents an author of a blog post.
    
    Attributes:
        full_name (str): The full name of the author.
        email (str): The unique email address of the author.
        bio (str): Optional biography of the author.
    """
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.full_name



class Blog(models.Model):
    """
    Represents a single blog post entry.

    Attributes:
        title (str): The title of the blog post.
        content (str): The main body content of the post.
        author (Author): The author of the blog post.
        created_at (datetime): Timestamp when the blog post was created.
        updated_at (datetime): Timestamp when the blog post was last updated.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title