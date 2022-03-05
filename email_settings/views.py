from .models import CommentFormNotification, NewUserEmailSetting
from django.core.mail import send_mail
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

# Create your views here.
@receiver(user_signed_up, dispatch_uid="8528816d-def2-41e5-8700-b079fc37c04d")
def user_signed_up(request, **kwargs):
	mail_obj = NewUserEmailSetting.objects.latest('id')
	send_mail(
		mail_obj.subject,
		mail_obj.message,
		f"{mail_obj.from_name} <{mail_obj.from_mail}>",
		[mail_obj.to_mail],
		fail_silently=False,
	)

def comment_email_setting():
	mail_obj = CommentFormNotification.objects.latest('id')
	send_mail(
		mail_obj.subject,
		mail_obj.message,
		f"{mail_obj.from_name} <{mail_obj.from_mail}>",
		[mail_obj.to_mail],
		fail_silently=False,
	)