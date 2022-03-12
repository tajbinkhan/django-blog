from django.contrib import admin
from .models import AllSetting

# Register your models here.
class AllSettingAdmin(admin.ModelAdmin):
	list_display = ('domain_name', 'site_name', 'protocol')
	save_on_top = True
	search_fields = ['domain_name']

admin.site.register(AllSetting, AllSettingAdmin)