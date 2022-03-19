from django.contrib import admin
from .models import AllSetting, EmailContent
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class AllSettingAdmin(ImportExportModelAdmin):
	list_display = ('domain_name', 'site_name', 'protocol')
	save_on_top = True
	search_fields = ['domain_name']

class EmailContentAdmin(ImportExportModelAdmin):
	list_display = ('notification_name', 'subject')
	save_on_top = True

admin.site.register(AllSetting, AllSettingAdmin)
admin.site.register(EmailContent, EmailContentAdmin)