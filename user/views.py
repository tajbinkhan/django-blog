from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm, UserDeleteForm
from allauth.account.views import PasswordChangeView, PasswordSetView, LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.db.models import Q

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, 'Your account has been updated successfully.')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)

@login_required
def deleteuser(request):
	if request.method == 'POST':
		delete_form = UserDeleteForm(request.POST, instance=request.user)
		user = request.user
		user.delete()
		messages.success(request, 'Your account has been deleted successfully.')
		return redirect('blog-home')
	else:
		delete_form = UserDeleteForm(instance=request.user)

	context = {
		'delete_form': delete_form
	}

	return render(request, 'users/delete_account.html', context)

class MyPasswordChangeView(PasswordChangeView):
	success_url = reverse_lazy('profile')

class MyPasswordSetView(PasswordSetView):
	success_url = reverse_lazy('profile')

class MyLoginView(LoginView):
	def form_invalid(self, form):
		username = self.request.POST.get('login')
		password = self.request.POST.get('password')

		try:
			user = User.objects.get(Q(username=username) | Q(email=username))
		except User.DoesNotExist:
			messages.error(self.request, 'Account does not exist.')
			return self.render_to_response(self.get_context_data(form=form))

		user = authenticate(self.request, username=username, password=password)

		if user is not None:
			if user.is_active:
				login(self.request, user)
				return redirect('blog-home')
			else:
				messages.error(self.request, 'This account is inactive.')
		else:
			messages.error(self.request, 'Incorrect password.')

		return self.render_to_response(self.get_context_data(form=form))