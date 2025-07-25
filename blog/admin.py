from django.contrib import admin
from .models import Author, Blog, Category
# Register your models here.


admin.site.site_header = "Blog Panel"



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'bio')
    search_fields = ('full_name', 'user__username')
    list_filter = ('user',)
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    search_fields = ('title', 'author__full_name')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

    

