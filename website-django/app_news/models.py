from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from app_users.models import Profile


class NewsCategory(models.Model):
    """Модель категории для новости"""
    category = models.CharField(max_length=100, verbose_name=_('Category'))

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class News(models.Model):
    """Модель ноовсти"""
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name=_('Category'))
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('Author'))
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.pk)])


class Comment(models.Model):
    """Модель комментария"""
    name = models.CharField(max_length=200, blank=True, verbose_name=_('Username'))
    comment = models.TextField(verbose_name=_('Comment'))
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('News'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))

    def __str__(self):
        return self.name
