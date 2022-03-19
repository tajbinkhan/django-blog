from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AllSetting(models.Model):
	domain_name = models.CharField(max_length=50)
	admin_email = models.EmailField(max_length=50, verbose_name='Admin Email')
	email_address = models.EmailField(max_length=50, verbose_name='Email Address')
	site_name = models.CharField(max_length=20)
	protocol = models.CharField(max_length=5)

	def __str__(self):
		return self.site_name

class EmailContent(models.Model):
	NOTIFICAITON_STATUS = [
		('New User Registration Notification', 'New User Registration Notification'),
		('New Comment Notification', 'New Comment Notification'),
		('Password Change Notification', 'Password Change Notification'),
	]
	subject = models.CharField(max_length=50)
	message = RichTextField()
	notification_name = models.CharField(max_length=256, choices=NOTIFICAITON_STATUS)

	def __str__(self):
		return self.notification_name