from django.contrib import admin

from app_news.models import News, NewsCategory


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
