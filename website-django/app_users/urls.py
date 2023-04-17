from django.urls import path
from django.views.decorators.cache import cache_page

from app_users.views import registration, MainLoginView, MainLogoutView, AccountInformationView

urlpatterns = [
    path('registration/', cache_page(3600)(registration), name='registration'),
    path('login/', cache_page(3600)(MainLoginView.as_view()), name='login'),
    path('logout/', MainLogoutView.as_view(), name='logout'),
    path('<str:username>/', AccountInformationView.as_view(), name='account'),

]
