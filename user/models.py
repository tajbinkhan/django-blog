import os
import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = datetime.datetime.now()
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'profile/{final_filename}'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to=upload_image_path)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class NewUserEmailSettings(models.Model):
	subject = models.CharField(max_length=25)
	message = models.TextField()
	from_mail = models.EmailField(max_length=50, verbose_name='From Mail')
	to_mail = models.EmailField(max_length=50, verbose_name='To Mail')

	def __str__(self):
		return self.subject

@receiver(user_signed_up, dispatch_uid="8528816d-def2-41e5-8700-b079fc37c04d")
def user_signed_up_(request, user, **kwargs):
	mail_obj = NewUserEmailSettings.objects.latest('id')
	send_mail(
		mail_obj.subject,
		mail_obj.message,
		mail_obj.from_mail,
		[mail_obj.to_mail],
		fail_silently=False,
	)