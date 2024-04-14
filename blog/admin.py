from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date_of_creation', 'view_count', 'is_published')
    list_filter = ('is_published',)
