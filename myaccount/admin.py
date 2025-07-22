from django.contrib import admin
from .models import User 

admin.site.site_header = "My Account Admin"
admin.site.site_title = "My Account Admin Portal"
admin.site.index_title = "Welcome to My Account Admin Portal"

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')

admin.site.register(User, UserAdmin)