from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from .models import Like, Rating, Comment


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'product')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'product', 'rating')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'product', 'text')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation


