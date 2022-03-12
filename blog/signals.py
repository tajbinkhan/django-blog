from django.dispatch import receiver
from .models import Post, Category, Comment
from email_settings.models import CommentFormNotification
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from site_setting.models import AllSetting

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

def pre_save_category_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_category_receiver, sender=Category)

@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
	site_obj = AllSetting.objects.latest('id')
	context = {
		'domain': site_obj.domain_name,
		'site_name': site_obj.site_name,
		'protocol': site_obj.protocol,
		'post': instance.post,
		'post_slug': instance.post.slug,
		'user': instance.user,
		'timestamp': instance.created_on
	}
	email_template_name = "email/new_comment_notification.txt"
	email = render_to_string(email_template_name, context)
	if created:
		mail_obj = CommentFormNotification.objects.latest('id')
		send_mail(
			mail_obj.subject,
			email,
			f"{mail_obj.from_name} <{mail_obj.from_mail}>",
			[mail_obj.to_mail],
			fail_silently=False,
		)