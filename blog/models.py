import os
import datetime
from PIL import Image
from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'blog-thumbnail/{final_filename}'

class Category(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "categories"
		ordering = ['-date_created']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_by_category', kwargs={'slug': self.slug})


class Post(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
	overview = models.TextField()
	content = RichTextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField(Category)
	img_thumbnail = models.ImageField(upload_to=upload_image_path)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	publish = models.BooleanField(default=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={"slug": self.slug})

	def get_comments(self):
		return self.comments.all().order_by('-created_on')

	def save(self):
		super().save()
		img = Image.open(self.img_thumbnail.path)
		if img.height > 426 or img.width > 640:
			output_size = (426, 640)
			img.thumbnail(output_size)
			img.save(self.img_thumbnail.path)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.user.username