from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.conf import settings
from django.core.mail import EmailMessage
from site_setting.models import AllSetting, EmailContent
from site_setting import utils

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

@receiver(post_save, sender=User)
def send_message(sender, instance, created, **kwargs):
	site_obj = AllSetting.objects.latest('id')
	email_obj = EmailContent.objects.filter(notification_name='New User Registration Notification').latest('id')
	context = {
		'domain': site_obj.domain_name,
		'site_name': site_obj.site_name,
		'username': instance.username,
		'first_name': instance.first_name,
		'last_name': instance.last_name,
		'email_address': instance.email,
		'timestamp': instance.date_joined,
		'protocol': site_obj.protocol,
		'admin_panel': settings.ADMIN_PANEL
	}
	if created:
		subject = email_obj.subject
		from_ = f"{site_obj.site_name} <{site_obj.email_address}>"
		html_content = utils.add_context_to_string(email_obj.message, context)
		to = [site_obj.admin_email]
		msg = EmailMessage(subject, html_content, from_, to)
		msg.content_subtype = "html"
		msg.send()

@receiver(pre_save, sender=User)
def comment_update(sender, instance, *args, **kwargs):
	site_obj = AllSetting.objects.latest('id')
	email_obj = EmailContent.objects.filter(notification_name='Password Change Notification').latest('id')
	context = {
		'domain': site_obj.domain_name,
		'site_name': site_obj.site_name,
		'username': instance.username,
		'email_address': instance.email,
		'protocol': site_obj.protocol,
	}
	if instance.pk:
		old_content = User.objects.get(pk=instance.pk)
		if not old_content.password == instance.password:
			subject = email_obj.subject
			from_ = f"{site_obj.site_name} <{site_obj.email_address}>"
			html_content = utils.add_context_to_string(email_obj.message, context)
			to = [site_obj.admin_email]
			msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()