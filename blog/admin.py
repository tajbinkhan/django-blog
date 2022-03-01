from django.contrib import admin
from .models import Post, Category, Comment, CommentFormNotification
from django.contrib.auth.models import Permission


class SaveOnTop(admin.ModelAdmin):
	save_on_top = True


class PostAdmin(SaveOnTop):
	list_display = ('title', 'timestamp', 'last_modified', 'previous_post', 'next_post')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(SaveOnTop):
	list_display = ('title', 'slug', 'date_created', 'last_modified')
	list_filter = ['date_created']
	search_fields = ['title']


class CommentAdmin(SaveOnTop):
	list_display = ('user', 'content', 'post', 'created_on')
	list_filter = ('created_on',)
	search_fields = ('user', 'content')


class CommentFormNotificationAdmin(SaveOnTop):
	list_display = ('subject', 'from_mail', 'to_mail')
	search_fields = ['user']

admin.site.site_header = 'Admin Panel'
admin.site.index_title = 'Blog Site Administration'
admin.site.site_title = 'Django Blog'
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentFormNotification, CommentFormNotificationAdmin)
admin.site.register(Permission)