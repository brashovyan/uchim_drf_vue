from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *
from rest_framework import routers
from .yasg import urlpatterns as doc_urls
from women import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Если мы хотим апи, то обращаемся по этому адресу
    path("api/v1/", include("women.urls")),

    # Если мы хотим фронт (обычный сайтик), то пишем любой запрос полсе /app/, он вызовет index.html, а там в свою очередь vue сам
    # разберётся какой адрес и чё выдать
    # re_path(r'app/*', TemplateView.as_view(template_name="index.html")),

    # Простой переброс на app/
    path('', RedirectView.as_view(url='/app/')),

    # вообще авторизацию можно впихнуть именно в приложение апи, но не суть
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += doc_urls

# это нужно для отображения картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
