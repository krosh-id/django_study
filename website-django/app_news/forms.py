from django import forms

from app_news.models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = 'title', 'description', 'category', 'image'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
