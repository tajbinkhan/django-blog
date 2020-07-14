from django.contrib import admin
from .models import Setting, FooterCredit

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
	list_display = ('title', 'email', 'facebook', 'instagram', 'youtube')
	save_on_top = True
	search_fields = ['title', 'email']

class FooterCreditAdmin(admin.ModelAdmin):
	list_display = ('title', 'left_credit', 'right_credit')
	save_on_top = True
	search_fields = ['title', 'left_credit', 'right_credit']

admin.site.register(Setting, SettingAdmin)
admin.site.register(FooterCredit, FooterCreditAdmin)
