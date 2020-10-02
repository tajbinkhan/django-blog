from django.urls import path
from django.urls import reverse_lazy
from .views import SearchListView

urlpatterns = [
	path('post/search/', SearchListView.as_view(), name='search'),
]