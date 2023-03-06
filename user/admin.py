from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission, Group
from .forms import UserModelForm

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	save_on_top = True
	search_fields = ['user']

class UserAdmin(UserAdmin):
	model = User
	add_form = UserModelForm
	ordering = ('-date_joined', )
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
		}),
	)

admin.site.unregister(User)
admin.site.unregister(Permission)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)