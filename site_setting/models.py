from django.db import models

# Create your models here.
class AllSetting(models.Model):
	domain_name = models.CharField(max_length=50)
	site_name = models.CharField(max_length=20)
	protocol = models.CharField(max_length=5)

	def __str__(self):
		return self.site_name