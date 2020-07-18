from django.db import models

# Create your models here.

class Setting(models.Model):
	title = models.CharField(max_length=120)
	footer_1 = models.TextField()
	email = models.EmailField(max_length=50)
	facebook = models.CharField(max_length=50)
	instagram = models.CharField(max_length=50)
	youtube = models.CharField(max_length=50)
	left_credit = models.CharField(max_length=120)
	right_credit = models.CharField(max_length=120)

	def __str__(self):
		return self.title