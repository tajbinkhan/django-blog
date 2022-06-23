from django.apps import AppConfig


class UserConfig(AppConfig):
	name = 'user'
	verbose_name = "User Profile"

	def ready(self):
		import user.signals
