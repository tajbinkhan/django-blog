from django.shortcuts import render
from .models import Setting, FooterCredit

# Create your views here.

def setting(request):
	site_setting = Setting.objects.all()
	context = {
		'site_setting': site_setting
	}
	return render(request, 'blog/footer.html', context)

def footer_credit(request):
	footer_setting = FooterCredit.objects.all()
	context = {
		'footer_setting': footer_setting
	}
	return render(request, 'blog/footer.html', context)