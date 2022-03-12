from django.apps import AppConfig


class BlogConfig(AppConfig):
	name = 'blog'
	verbose_name = "Blog Posts & Comments"

	def ready(self):
		import blog.signals
