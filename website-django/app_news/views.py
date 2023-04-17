from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets, permissions

from app_news.forms import NewsForm, CommentForm
from app_news.models import News, Comment, NewsCategory
from app_news.permissions import IsAdminOrIsOwner
from app_news.serializers import NewsSerializer


class MainPage(generic.ListView):
    """Представление главной страницы, которая отображает список всех новостей"""
    model = News
    context_object_name = 'news_list'
    template_name = 'site/main_page.html'
    queryset = News.objects.all().order_by('-updated_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsCategory.objects.all()
        return context


class NewsByCategory(generic.ListView):
    """Представление, отображающее новости по категориям"""
    model = News
    context_object_name = 'news_list'
    template_name = 'site/category.html'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsCategory.objects.all()
        context['title'] = NewsCategory.objects.get(id=self.kwargs['category_id'])
        return context


class CreateNews(generic.CreateView):
    """Представление для создания новости"""
    model = News
    form_class = NewsForm
    template_name = 'site/create_news.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user.profile
        self.object.save()
        self.request.user.profile.news_quantity += 1
        self.request.user.profile.save()
        return HttpResponseRedirect(self.get_success_url())


class NewsDetail(generic.DetailView):
    """Представление, отображающее определенную новость"""
    model = News
    template_name = 'site/news_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_comments'] = Comment.objects.all()
        context['comment_form'] = CommentForm()
        context['categories'] = NewsCategory.objects.all()
        return context

    def post(self, request, pk, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                comment = comment_form.save(commit=False)
                comment.name = request.user.username
                news = self.get_object()
                comment.news = news
                comment.user = request.user
                request.user.profile.comment_quantity += 1
                request.user.profile.save()
                comment.save()
                return HttpResponseRedirect(reverse_lazy('news_detail', kwargs={'pk': pk}))
            else:
                raise PermissionDenied()
        else:
            return render(request, 'site/news_detail.html', context={
                'comment_form': comment_form, 'object': self.get_object()
            })


class UpdateNews(UserPassesTestMixin, generic.UpdateView):
    """Представление, для обновления новости"""
    model = News
    template_name = 'site/news_update.html'
    fields = ['title', 'description', 'category']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user.profile


class NewsViewSet(viewsets.ModelViewSet):
    """Представление для получения списка новостей, а также создания, обновления и удаления определенной новости"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'list': (permissions.AllowAny,),
        'retrieve': (permissions.AllowAny,),
        'update': (IsAdminOrIsOwner,),
        'partial_update': (IsAdminOrIsOwner,),
        'destroy': (IsAdminOrIsOwner,)
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
