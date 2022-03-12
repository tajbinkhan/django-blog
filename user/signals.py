from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.conf import settings
from django.template.loader import render_to_string
from email_settings.models import NewUserEmailSetting
from django.core.mail import send_mail
from site_setting.models import AllSetting

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
	email_template_name = "email/new_user_notification.txt"
	email = render_to_string(email_template_name, context)
	if created:
		mail_obj = NewUserEmailSetting.objects.latest('id')
		send_mail(
			mail_obj.subject,
			email,
			f"{mail_obj.from_name} <{mail_obj.from_mail}>",
			[mail_obj.to_mail],
			fail_silently=False,
		)

@receiver(pre_save, sender=User)
def comment_update(sender, instance, *args, **kwargs):
	site_obj = AllSetting.objects.latest('id')
	context = {
		'domain': site_obj.domain_name,
		'site_name': site_obj.site_name,
		'username': instance.username,
		'email_address': instance.email,
		'protocol': site_obj.protocol,
	}
	email_template_name = "email/password_change_notification.txt"
	email = render_to_string(email_template_name, context)
	if instance.pk:
		old_content = User.objects.get(pk=instance.pk)
		if not old_content.password == instance.password:
			send_mail(
				'Password Change Notification',
				email,
				f"Django Blog <info@webphics.com>",
				[instance.email],
				fail_silently=False,
			)