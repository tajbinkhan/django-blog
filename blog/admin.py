from django.contrib import admin
from .models import Post, Category, Comment
from django.contrib.auth.models import Permission
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PostAdmin(ImportExportModelAdmin):
	list_display = ('title', 'timestamp', 'last_modified')
	save_on_top = True
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(ImportExportModelAdmin):
	list_display = ('title', 'slug', 'date_created', 'last_modified')
	save_on_top = True
	list_filter = ['date_created']
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(ImportExportModelAdmin):
	list_display = ('user', 'content', 'post', 'created_on')
	save_on_top = True
	list_filter = ('created_on',)
	search_fields = ('user', 'content')

admin.site.site_header = 'Admin Panel'
admin.site.index_title = 'Blog Site Administration'
admin.site.site_title = 'Django Blog'
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Permission)