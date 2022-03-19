from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProfileAdmin(ImportExportModelAdmin):
	list_display = ('user',)
	save_on_top = True
	search_fields = ['user']

class MyUserAdmin(ImportExportModelAdmin):
	ordering = ('-date_joined', )
	list_display = ('username', 'email', 'date_joined', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Profile, ProfileAdmin)