from django.urls import path
from django.views.decorators.cache import cache_page

from app_news.views import CreateNews, NewsDetail, UpdateNews, NewsByCategory

urlpatterns = [
    path('create_news/', cache_page(3600)(CreateNews.as_view()), name='create_news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('update_news/<int:pk>/', UpdateNews.as_view(), name='update_news'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='news_by_category')
]
