import os
import random
import string
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post, Category, Comment
from django.utils.decorators import method_decorator
from .decorators import superuser_required
from .forms import CommentForm, PostForm, CategoryForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.text import slugify
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

def error(request, exception):
	context = {
		'head_title': 'Not found',
	}
	return render(request, 'error.html', context)

def privacy_policy(request):
	context = {
		'head_title': 'Privacy Policy',
	}
	return render(request, 'blog/privacy_policy.html', context)

def terms_of_service(request):
	context = {
		'head_title': 'Terms of Service',
	}
	return render(request, 'blog/terms_of_service.html', context)

@superuser_required
def duplicate_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	post_img = post.img_thumbnail.path
	if os.path.exists(post_img):
		new_post = Post.objects.create(
			title=post.title + ' (Copy)',
			slug=slugify(post.title) + '-copy',
			img_thumbnail=post.img_thumbnail,
			overview=post.overview,
			content=post.content,
			author=post.author,
		)
		for category in post.categories.all():
			new_post.categories.add(category)
	else:
		messages.error(request, 'Can not duplicate. Post image was not found.')
	return redirect('blog-home')

@superuser_required
def photos(request):
	photo_root = settings.MEDIA_ROOT
	photo_url = settings.MEDIA_URL
	website_url = request.scheme + '://' + request.get_host()
	photos = []

	for dirpath, dirnames, filenames in os.walk(photo_root):
		for filename in filenames:
			if not filename.startswith('.'):
				photo_file_path = os.path.join(dirpath, filename)
				photo_rel_path = os.path.relpath(photo_file_path, photo_root).replace("\\", "/")
				file_extension = os.path.splitext(filename)[1].lower()
				if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.eps']:
					photos.append({
						'url': website_url + photo_url + photo_rel_path,
						'filename': filename,
						'path': photo_rel_path,
						'date': os.path.getmtime(os.path.join(dirpath, filename))
					})

	photos = sorted(photos, key=lambda k: k['date'], reverse=True)
	paginator = Paginator(photos, 10)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.method == 'POST':
		file_to_delete = request.POST.get('file_to_delete')
		if file_to_delete:
			os.remove(os.path.join(photo_root, file_to_delete.replace("/", "\\")))
			messages.success(request, f"{file_to_delete} deleted successfully.")
			return redirect('photos')

	context = {
		'page_obj': page_obj,
	}

	return render(request, 'media_content/photos.html', context)

@superuser_required
def media_files(request):
	media_root = settings.MEDIA_ROOT
	media_url = settings.MEDIA_URL
	website_url = request.scheme + '://' + request.get_host()
	media_files = []

	for dirpath, dirnames, filenames in os.walk(media_root):
		for filename in filenames:
			if not filename.startswith('.'):
				media_file_path = os.path.join(dirpath, filename)
				media_rel_path = os.path.relpath(media_file_path, media_root).replace("\\", "/")
				file_extension = os.path.splitext(filename)[1].lower()
				if not file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.eps']:
					media_files.append({
						'url': website_url + media_url + media_rel_path,
						'filename': filename,
						'path': media_rel_path,
						'date': os.path.getmtime(os.path.join(dirpath, filename))
					})

	media_files = sorted(media_files, key=lambda k: k['date'], reverse=True)
	paginator = Paginator(media_files, 10)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.method == 'POST':
		file_to_delete = request.POST.get('file_to_delete')
		if file_to_delete:
			os.remove(os.path.join(media_root, file_to_delete.replace("/", "\\")))
			messages.success(request, f"{file_to_delete} deleted successfully.")
			return redirect('media_files')

	context = {
		'page_obj': page_obj,
	}
	return render(request, 'media_content/media_files.html', context)

@superuser_required
def upload_file(request):
	if request.method == 'POST':
		uploaded_files = request.FILES.getlist('files')
		for uploaded_file in uploaded_files:
			filename = uploaded_file.name
			filepath = os.path.join(settings.MEDIA_ROOT, filename)

			# If the file already exists, add a random 6-digit number to the end of the filename
			if os.path.exists(filepath):
				random_suffix = ''.join(random.choices(string.digits, k=6))
				filename = f"{os.path.splitext(filename)[0]}_{random_suffix}{os.path.splitext(filename)[1]}"
				filepath = os.path.join(settings.MEDIA_ROOT, filename)

			with open(filepath, 'wb+') as destination:
				for chunk in uploaded_file.chunks():
					destination.write(chunk)
		filename, extension = os.path.splitext(uploaded_files[-1].name)
		messages.success(request, 'File(s) uploaded successfully.')
		if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.eps']:
			return redirect('photos')
		else:
			return redirect('media_files')
	else:
		return render(request, 'media_content/upload_file.html')

class PostCategoryView(ListView):
	model = Post
	template_name = 'blog/category.html'
	context_object_name = 'categories'
	paginate_by = 4
	paginate_orphans = 2

	def get_queryset(self):
		self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
		return Post.objects.filter(categories = self.category)

	def get_context_data(self, **kwargs):
		context = super(PostCategoryView, self).get_context_data(**kwargs)
		context['category'] = self.category
		return context

class PostListView(ListView):
	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 4
	paginate_orphans = 2

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = queryset.filter(publish=True)
		return queryset

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'posts'
	form = CommentForm()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.form
		return context

	def post(self, request, *args, **kwargs):
		form = CommentForm(request.POST)
		if form.is_valid():
			post = self.get_object()
			form.instance.user = request.user
			form.instance.post = post
			form.save()
			return redirect(reverse('post_detail', kwargs={'slug': post.slug}))

@method_decorator(superuser_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, CreateView):
	model = Post
	template_name = 'blog/post_form.html'
	form_class = PostForm
	permission_required = 'blog.fields'
	success_message = "%(title)s was created successfully"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create'
		context['submit'] = 'Create Post'
		context['head_title'] = 'Create Post'
		return context

@method_decorator(superuser_required, name='dispatch')
class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('blog-home')
	success_message = "Post was deleted successfully"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete'
		context['submit'] = 'Delete Post'
		context['head_title'] = 'Delete Post'
		return context

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

@method_decorator(superuser_required, name='dispatch')
class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = PostForm
	success_message = "%(title)s was updated successfully"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update'
		context['submit'] = 'Update Post'
		context['head_title'] = 'Update Post'
		return context

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

@method_decorator(superuser_required, name='dispatch')
class CategoryListView(LoginRequiredMixin, ListView):
	model = Category
	template_name = 'blog/category_list_form.html'
	context_object_name = 'category'
	ordering = ['-id']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lists of Category'
		context['head_title'] = 'Lists of Category'
		return context

@method_decorator(superuser_required, name='dispatch')
class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, CreateView):
	model = Category
	template_name = 'blog/category_form.html'
	form_class = CategoryForm
	permission_required = 'blog.fields'
	success_url = reverse_lazy('category_list')
	success_message = "Category %(title)s was created successfully"

	def form_valid(self, form):
		category_form = super(CategoryCreateView, self).form_valid(form)
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add New Category'
		context['submit'] = 'Create Category'
		context['head_title'] = 'Add new category'
		return context

@method_decorator(superuser_required, name='dispatch')
class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('category_list')
	success_message = "Category %(title)s was updated successfully"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Category'
		context['submit'] = 'Update Category'
		context['head_title'] = 'Edit Category'
		return context

	def test_func(self):
		category = self.get_object()
		if self.request.user == category.author:
			return True
		return False

@method_decorator(superuser_required, name='dispatch')
class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Category
	success_url = reverse_lazy('category_list')
	success_message = "Category %(title)s was updated successfully"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Category'
		context['submit'] = 'Delete Category'
		context['head_title'] = 'Delete Category'
		return context

	def test_func(self):
		category = self.get_object()
		if self.request.user == category.author:
			return True
		return False

@method_decorator(superuser_required, name='dispatch')
class CommentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	form_class = CommentForm
	success_message = "Comment was updated successfully"
	template_name = 'blog/comment_edit.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		post = self.object.post
		return reverse_lazy('post_detail', kwargs={'slug': post.slug})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Comment'
		context['submit'] = 'Update Comment'
		context['head_title'] = 'Update Comment'
		return context

	def test_func(self):
		if self.request.user.is_superuser:
			return True
		return False

@method_decorator(superuser_required, name='dispatch')
class CommentDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	success_message = "Comment was deleted successfully"
	template_name = 'blog/comment_delete.html'

	def get_success_url(self):
		post = self.object.post
		return reverse_lazy('post_detail', kwargs={'slug': post.slug})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete'
		context['head_title'] = 'Delete Comment'
		return context

	def test_func(self):
		if self.request.user.is_superuser:
			return True
		return False