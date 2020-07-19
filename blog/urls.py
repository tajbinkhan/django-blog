from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, PostCategoryView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, SearchListView

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('post/', RedirectView.as_view(url=reverse_lazy('blog-home'), permanent=False)),
	path('post/category/', RedirectView.as_view(url=reverse_lazy('blog-home'), permanent=False)),
	path('post/create/', PostCreateView.as_view(), name='post_create'),
	path('post/category/create/', CategoryCreateView.as_view(), name='category_create'),
	path('post/category/list/', CategoryListView.as_view(), name='category_list'),
	path('post/category/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
	path('post/category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
	path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
	path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
	path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('post/category/<slug:slug>/', PostCategoryView.as_view(), name='post_by_category'),
	path('search/', SearchListView.as_view(), name='search'),
	path('tinymce/', include('tinymce.urls')),
]

handler404 = 'blog.views.error_404_page'