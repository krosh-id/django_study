from rest_framework import serializers

from app_news.models import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = ['title', 'description', 'category', 'author']
