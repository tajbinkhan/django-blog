from django import forms
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.forms import UserCreationForm


class UserModelForm(UserCreationForm):
	class Meta:
		model = User
		fields = "__all__"


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ["image"]


class UserDeleteForm(forms.ModelForm):
	class Meta:
		model = User
		fields = []


class CustomSignupForm(SignupForm):
	first_name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={"placeholder": "Enter your first name"}),
	)
	last_name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={"placeholder": "Enter your last name"}),
	)

	field_order = [
		"username",
		"first_name",
		"last_name",
		"email",
		"password1",
		"password2",
	]

	def save(self, request):
		user = super(CustomSignupForm, self).save(request)
		if not user:
			return user
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.save()
		return user


class CustomLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		super(CustomLoginForm, self).__init__(*args, **kwargs)
		self.fields["login"].widget.attrs.update(
			{"placeholder": "Username or Email", "class": "textinput form-control"}
		)
		self.fields["login"].label = "Username or Email"
		self.fields["remember"].widget.attrs.update({"checked": "true"})
