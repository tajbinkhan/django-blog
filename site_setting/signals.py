from django.dispatch import receiver
from blog.models import Comment
from .models import AllSetting, EmailContent
from django.db.models.signals import pre_save, post_save
from .utils import add_context_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User

# Blog Model
@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
	site_obj = AllSetting.objects.last()
	if site_obj:
		email_obj = EmailContent.objects.filter(notification_name='New Comment Notification').last()
		context = {
			'domain': site_obj.domain_name,
			'site_name': site_obj.site_name,
			'protocol': site_obj.protocol,
			'subject': email_obj.subject,
			'post': instance.post,
			'comment': instance.content,
			'post_slug': instance.post.slug,
			'user': instance.user,
			'timestamp': instance.created_on
		}
		if created:
			subject = email_obj.subject
			from_ = f"{site_obj.site_name} <{site_obj.email_address}>"
			to = [site_obj.admin_email]
			if email_obj.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_obj.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_obj.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	else:
		pass

# User Model
@receiver(post_save, sender=User)
def new_user_notification(sender, instance, created, **kwargs):
	site_obj = AllSetting.objects.last()
	if site_obj:
		email_obj = EmailContent.objects.filter(notification_name='New User Registration Notification').last()
		context = {
			'domain': site_obj.domain_name,
			'site_name': site_obj.site_name,
			'subject': email_obj.subject,
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
			to = [site_obj.admin_email]
			if email_obj.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_obj.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_obj.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	else:
		pass

@receiver(pre_save, sender=User)
def user_password_update(sender, instance, *args, **kwargs):
	site_obj = AllSetting.objects.last()
	if site_obj:
		email_obj = EmailContent.objects.filter(notification_name='Password Change Notification').last()
		context = {
			'domain': site_obj.domain_name,
			'site_name': site_obj.site_name,
			'username': instance.username,
			'email_address': instance.email,
			'protocol': site_obj.protocol,
			'subject': email_obj.subject
		}
		if instance.pk:
			old_content = User.objects.get(pk=instance.pk)
			if not old_content.password == instance.password:
				subject = email_obj.subject
				from_ = f"{site_obj.site_name} <{site_obj.email_address}>"
				to = [instance.email]
				if email_obj.plain_text_html_enable == True:
					plain_html_content = add_context_to_string(email_obj.plain_text_html, context)
					msg = EmailMessage(subject, plain_html_content, from_, to)
				else:
					html_content = add_context_to_string(email_obj.message, context)
					msg = EmailMessage(subject, html_content, from_, to)
				msg.content_subtype = "html"
				msg.send()
	else:
		pass