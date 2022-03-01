from .models import Post
from django.db.models import Count


def get_category_count():
	"""
	Hits DB on each request. Will cause performance issues on high load
	"""
	category_query = Post.objects.values('categories__slug', 'categories__title').annotate(Count('categories__title'))
	return category_query


def sidebar(request):
	"""
	Hits DB on each request. Will cause performance issues on high load
	"""
	category_count = get_category_count()
	most_recent = Post.objects.order_by('-timestamp')[:3]
	context = {
		'most_recent': most_recent,
		'category_count': category_count,
	}
	return context
