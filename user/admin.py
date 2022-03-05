from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	save_on_top = True
	search_fields = ['user']

class MyUserAdmin(UserAdmin):
	ordering = ('-date_joined', )
	list_display = ('username', 'email', 'date_joined', 'first_name', 'last_name', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Profile, ProfileAdmin)