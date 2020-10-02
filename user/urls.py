from django.urls import path, include
from . import views
from .views import register, login_page, logout_page, profile, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),
	path('profile/', views.profile, name='profile'),
	path('change-password/', PasswordChangeView.as_view(), name='password_change'),
	path('change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
	path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
