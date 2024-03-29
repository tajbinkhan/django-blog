from django.apps import AppConfig


class SiteSettingConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "site_setting"
	verbose_name = "Site Settings"

	def ready(self):
		import site_setting.signals
