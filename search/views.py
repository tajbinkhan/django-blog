from django.db.models import Count, Q
from django.shortcuts import render
from blog.models import Post
from blog.views import get_category_count
from django.views.generic import ListView

# Create your views here.

class SearchListView(ListView):
	model = Post
	template_name = 'blog/search_result.html'
	context_object_name = 'search_queryset'
	paginate_by = 6

	def get_context_data(self, *args, **kwargs):
		category_count = get_category_count()
		most_recent = Post.objects.order_by('-timestamp')[:3]
		context = super(SearchListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		context['head_title'] = 'Search'
		context['most_recent'] = most_recent
		context['category_count'] = category_count
		context['query'] = self.request.GET.get('q')
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		query = request.GET.get('q')
		if query is not None:
			lookups = (Q(title__icontains=query) | 
				Q(content__icontains=query) | 
				Q(categories__title__icontains=query))
		else:
			return Post.objects.all()
		return Post.objects.filter(lookups).distinct().order_by('-timestamp')
