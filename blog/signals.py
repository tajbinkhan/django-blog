from .models import Post, Category
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

def pre_save_category_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_category_receiver, sender=Category)