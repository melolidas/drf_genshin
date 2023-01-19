from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

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
]
