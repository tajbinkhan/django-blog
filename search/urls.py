from django.urls import path
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from .views import SearchListView

urlpatterns = [
	path('search/', SearchListView.as_view(), name='search'),
]