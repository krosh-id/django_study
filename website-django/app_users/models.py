from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """Модель профиля"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    news_quantity = models.IntegerField(default=0, verbose_name=_("News quantity"))
    comment_quantity = models.IntegerField(default=0, verbose_name=_('Comments quantity'))

    def __str__(self):
        return str(self.user)
