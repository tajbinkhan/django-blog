from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post, Category
from .forms import CommentForm, PostForm, CategoryForm

# Create your views here.

def get_category_count():
    category_query = Post.objects.values('categories__slug', 'categories__title').annotate(Count('categories__title'))
    return category_query

class PostCategoryView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'categories'
    ordering = ['-date_created']
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(categories = self.category)

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super(PostCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        return context

class SearchView(View):
    def get(self, request, *args, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        paginate_by = 6
        search_queryset = Post.objects.all().order_by('-timestamp')
        search_query = request.GET.get('q')
        if search_query:
            search_queryset = search_queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            ).distinct()

        context = {
            'category_count': category_count,
            'search_queryset': search_queryset,
            'most_recent': most_recent,
            'head_title': 'Search',
        }

        return render(request, 'blog/search_result.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-timestamp']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    form = CommentForm()

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
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

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    permission_required = 'blog.fields'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        context['title'] = 'Create'
        context['submit'] = 'Create Post'
        context['head_title'] = 'Create Post'
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        context['title'] = 'Update'
        context['submit'] = 'Update Post'
        context['head_title'] = 'Update Post'
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list_form.html'
    context_object_name = 'category'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        context['title'] = 'Lists of Category'
        context['head_title'] = 'Lists of Category'
        return context

class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    template_name = 'blog/category_form.html'
    form_class = CategoryForm
    permission_required = 'blog.fields'
    success_url = reverse_lazy('post_create')

    def form_valid(self, form):
        category_form = super(CategoryCreateView, self).form_valid(form)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        context['title'] = 'Add New Category'
        context['submit'] = 'Create Category'
        context['head_title'] = 'Add new category'
        return context

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['category_count'] = category_count
        context['title'] = 'Edit Category'
        context['submit'] = 'Update Category'
        context['head_title'] = 'Edit Category'
        return context

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False