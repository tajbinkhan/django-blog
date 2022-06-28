from blog.models import Post
from django.db.models import Count
from .models import AllSetting

def get_category_count():
	category_query = Post.objects.values('categories__slug', 'categories__title').annotate(Count('categories__title'))
	return category_query

def sidebar(request):
	category_count = get_category_count()
	most_recent = Post.objects.order_by('-timestamp')[:3]
	settings = AllSetting.objects.last()
	context = {
		'most_recent': most_recent,
		'category_count': category_count,
		'settings': settings,
	}
	return context