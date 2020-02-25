from django.contrib import admin
from .models import Post, Comment , Reply

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','image')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name','body')
    # actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(active=True)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on')
    list_filter = ( 'created_on',)
    search_fields = ('name','body')

    



admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Reply,ReplyAdmin)