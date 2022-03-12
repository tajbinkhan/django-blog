from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostDeleteView,
	PostUpdateView,
	PostCategoryView,
	CategoryListView,
	CategoryCreateView,
	CategoryUpdateView,
	CategoryDeleteView,
	CommentDeleteView,
	CommentUpdateView)

urlpatterns = [
	path('post/', RedirectView.as_view(url=reverse_lazy('blog-home'), permanent=False)),
	path('', PostListView.as_view(), name='blog-home'),
	path('post/create/', PostCreateView.as_view(), name='post_create'),
	path('category/create/', CategoryCreateView.as_view(), name='category_create'),
	path('category/list/', CategoryListView.as_view(), name='category_list'),
	path('category/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
	path('category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
	path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
	path('<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
	path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('category/<slug:slug>/', PostCategoryView.as_view(), name='post_by_category'),
	path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
	path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]