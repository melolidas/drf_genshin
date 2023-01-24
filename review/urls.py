from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet, RatingViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('likes', LikeViewSet)
router.register('ratings', RatingViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]