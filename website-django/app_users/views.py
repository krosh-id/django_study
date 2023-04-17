from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView

from app_users.forms import SignUpForm
from app_users.models import Profile


def registration(request):
    """Функция, для регистрации нового пользователя"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('main_page'))
    else:
        form = SignUpForm()
    return render(request, 'users/registration.html', {'form': form})


class MainLoginView(LoginView):
    """Представление, для авторизации пользователя"""
    template_name = 'users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('account', kwargs={'username': self.request.user.username})


class MainLogoutView(LogoutView):
    """Представление, для выхода из логина"""
    next_page = reverse_lazy('main_page')


class AccountInformationView(DetailView):
    """Представление, отображает профиль пользователя"""
    model = Profile
    template_name = 'users/account.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
