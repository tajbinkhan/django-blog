import os
from django.dispatch import receiver
from .models import Post, Category
from django.db.models.signals import pre_save, post_delete
from .utils import unique_slug_generator

def _delete_file(path):
	if os.path.isfile(path):
		os.remove(path)

@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

@receiver(post_delete, sender=Post)
def post_delete_post_thumbnail_receiver(sender, instance, *args, **kwargs):
	if instance.img_thumbnail:
		_delete_file(instance.img_thumbnail.path)

@receiver(pre_save, sender=Category)
def pre_save_category_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)