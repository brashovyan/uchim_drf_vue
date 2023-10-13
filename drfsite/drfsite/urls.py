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
    path('api/v1/admin/', admin.site.urls),
    path("api/v1/", include("women.urls")),

    # крч, всё, что относится к бэку - это api/v1/, media/ и static/
    # всё остальное примет на себя фронт

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    # окей, это исключение
    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += doc_urls

# это нужно для отображения картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
