from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog.views import privacy_policy, terms_of_service
from user.views import MyPasswordChangeView, MyPasswordSetView
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('admin/', admin.site.urls),
	path('privacy-policy/', privacy_policy, name='privacy-policy'),
	path('terms-of-service/', terms_of_service, name='terms-of-service'),
	path('', include('blog.urls')),
	path('post/', include('search.urls')),
	path('user/', include('user.urls')),
	path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
	path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),
	path('accounts/', include('allauth.urls')),
	path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'blog.views.error'