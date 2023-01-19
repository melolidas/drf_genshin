"account urls.py"
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterAPIView



urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
]