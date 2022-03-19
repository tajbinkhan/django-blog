from django.dispatch import receiver
from .models import Post, Category, Comment
from site_setting.models import AllSetting, EmailContent
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from site_setting import utils
from django.core.mail import EmailMessage

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
		'comment': instance.content,
		'post_slug': instance.post.slug,
		'user': instance.user,
		'timestamp': instance.created_on
	}
	if created:
		site_obj = AllSetting.objects.latest('id')
		email_obj = EmailContent.objects.filter(notification_name='New Comment Notification').latest('id')
		subject = email_obj.subject
		from_ = f"{site_obj.site_name} <{site_obj.email_address}>"
		html_content = utils.add_context_to_string(email_obj.message, context)
		to = [site_obj.admin_email]
		msg = EmailMessage(subject, html_content, from_, to)
		msg.content_subtype = "html"
		msg.send()