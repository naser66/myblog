from django.contrib import admin
from .models import Post, BlogGroup


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'group', 'status', 'datetime_edit', )
    ordering = ('status',)


class BlogGroupAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(BlogGroup, BlogGroupAdmin)
