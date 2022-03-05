from django.contrib import admin
from .models import CommentFormNotification, NewUserEmailSetting

# Register your models here.
class NewUserEmailSettingsAdmin(admin.ModelAdmin):
	list_display = ('subject', 'from_name', 'from_mail', 'to_mail')
	save_on_top = True
	search_fields = ['user']

class CommentFormNotificationAdmin(admin.ModelAdmin):
	list_display = ('subject', 'from_name', 'from_mail', 'to_mail')
	save_on_top = True
	search_fields = ['user']

admin.site.register(NewUserEmailSetting, NewUserEmailSettingsAdmin)
admin.site.register(CommentFormNotification, CommentFormNotificationAdmin)