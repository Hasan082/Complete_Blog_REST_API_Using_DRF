from django.contrib import admin
from .models import Author, Blog
# Register your models here.


admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to the Blog Admin Portal"

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'bio')
    search_fields = ('full_name', 'email')
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('author',)
    
    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
