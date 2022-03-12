from django.shortcuts import redirect, render

def superuser_required(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_superuser:
			return function(request, *args, **kwargs)
		else:
			return render(request, 'error.html')
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def login_redirect(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			return function(request, *args, **kwargs)
		else:
			return redirect('profile')
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap