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
	plain_text_html = models.TextField(verbose_name='Plain Text HTML')
	message = RichTextField()
	notification_name = models.CharField(max_length=256, choices=NOTIFICAITON_STATUS)
	plain_text_html_enable = models.BooleanField(verbose_name='Plain Text HTML Enable', help_text='This will ignore the message field content.')

	def __str__(self):
		return self.notification_name