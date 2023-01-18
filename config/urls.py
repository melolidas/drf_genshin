from django.contrib import admin
from django.urls import path

from account.views import RegisterAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/register/', RegisterAPIView.as_view()),
]
