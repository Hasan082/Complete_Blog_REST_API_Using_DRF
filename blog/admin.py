from django.contrib import admin
from .models import Author, Blog, Category, Comment
# Register your models here.


admin.site.site_header = "Admin Panel"


    
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)