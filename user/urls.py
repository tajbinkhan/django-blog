from django.urls import path
from .views import profile, deleteuser

urlpatterns = [
	path('profile/', profile, name='profile'),
	path('eliminate/', deleteuser, name='delete-user')
]