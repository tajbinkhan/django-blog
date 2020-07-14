from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, SearchView, PostCategoryView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('post/create/', PostCreateView.as_view(), name='post_create'),
	path('post/category/create/', CategoryCreateView.as_view(), name='category_create'),
	path('post/category/list/', CategoryListView.as_view(), name='category_list'),
	path('post/category/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
	path('post/category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
	path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
	path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
	path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('post/category/<slug:slug>/', PostCategoryView.as_view(), name='post_by_category'),
	path('search/', SearchView.as_view(), name='search'),
	# path('admin-profile/', AdminProfileView.as_view(), name='admin_profile'),
	path('tinymce/', include('tinymce.urls')),
]