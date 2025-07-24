import os
import uuid
from django.utils.text import slugify


def profile_image_upload_to(instance, filename="profile_images"):
    ext = filename.split('.')[-1]
    base = slugify(getattr(instance, 'full_name', 'profile'))
    unique_name = f"{base}-{uuid.uuid4().hex[:8]}.{ext}"
    return os.path.join("profiles", unique_name)


def blog_image_upload_to(instance, filename="blog_images"):
    ext = filename.split('.')[-1]
    base = slugify(getattr(instance, 'title', 'blog'))
    unique_name = f"{base}-{uuid.uuid4().hex[:8]}.{ext}"
    return os.path.join("blogs", unique_name)
