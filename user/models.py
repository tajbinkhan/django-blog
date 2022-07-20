import os
import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
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