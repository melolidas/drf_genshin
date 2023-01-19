from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from heroes.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

router = routers.DefaultRouter()
router.register('hero', HeroViewSet, basename='hero')


swagger_view = get_schema_view(
    openapi.Info(
        title="genshin",
        default_version='v1',
        description="genshin"
    ),
    public=True
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('docs/', swagger_view.with_ui('swagger', cache_timeout=0)),
    path('', include('main.urls')),
    path('', include('review.urls')),
    path('api/v1/', include(router.urls)),
]

"""Подключение media и static"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
