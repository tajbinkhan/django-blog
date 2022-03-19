from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Enter post title (required)'
			}
		)
	)
	slug = forms.CharField(
		required = False,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Post slug (keep empty)',
			}
		)
	)
	overview = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Give an overview of the post (It will display in the post list)',
			}
		)
	)
	content = forms.CharField(
		widget=CKEditorWidget(
			attrs={
				'placeholder': 'Here goes post content in it',
			}
		)
	)

	class Meta:
		model = Post
		fields = ('title', 'slug', 'overview', 'content', 'img_thumbnail', 'categories', 'publish')

class CategoryForm(forms.ModelForm):
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Enter post category title (required)'
			}
		)
	)
	slug = forms.CharField(
		required = False,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Post category slug (keep empty)',
			}
		)
	)

	class Meta:
		model = Category
		fields = ('title', 'slug',)

class CommentForm(forms.ModelForm):
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'form_control text-appear',
				'placeholder': 'Type your comment',
				'id': 'usercomment',
				'rows': '4',
				'cols': '90'
			}
		)
	)
	class Meta:
		model = Comment
		fields = ('content',)