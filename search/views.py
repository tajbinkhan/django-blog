from django.db.models import Q
from blog.models import Post
from django.views.generic import ListView

# Create your views here.

class SearchListView(ListView):
	model = Post
	template_name = 'blog/search_result.html'
	context_object_name = 'search_queryset'
	paginate_by = 6

	def get_context_data(self, *args, **kwargs):
		context = super(SearchListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		context['head_title'] = 'Search'
		context['query'] = query
		return context

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get('q')
		if query is not None:
			lookups = (Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(categories__title__icontains=query))
		else:
			return Post.objects.all()
		return Post.objects.filter(lookups).distinct().order_by('-timestamp')
