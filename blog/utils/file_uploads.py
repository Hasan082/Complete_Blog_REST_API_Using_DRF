import os
import uuid
from django.utils.text import slugify

def unique_image_path(instance, filename, folder="uploads"):
    ext = filename.split('.')[-1]
    base = slugify(getattr(instance, 'title', 'image'))
    unique_name = f"{base}-{uuid.uuid4().hex[:8]}.{ext}"
    return os.path.join(folder, unique_name)
