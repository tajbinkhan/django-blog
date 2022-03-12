from django.db import models

# Create your models here.
class NewUserEmailSetting(models.Model):
	subject = models.CharField(max_length=25)
	from_name = models.CharField(max_length=50, verbose_name='From Name')
	from_mail = models.EmailField(max_length=50, verbose_name='From Mail')
	to_mail = models.EmailField(max_length=50, verbose_name='To Mail')

	def __str__(self):
		return self.subject

class CommentFormNotification(models.Model):
	subject = models.CharField(max_length=25)
	from_name = models.CharField(max_length=50, verbose_name='From Name')
	from_mail = models.EmailField(max_length=50, verbose_name='From Mail')
	to_mail = models.EmailField(max_length=50, verbose_name='To Mail')

	def __str__(self):
		return self.subject