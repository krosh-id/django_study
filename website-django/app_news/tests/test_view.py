from django.test import TestCase
from django.urls import reverse
from app_users.models import Profile
from django.contrib.auth.models import User
from app_news.models import NewsCategory, News, Comment


class SiteTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test1')
        user.set_password('test1')
        user.save()
        Profile.objects.create(user=user)
        category = NewsCategory.objects.create(category='Спорт')
        News.objects.create(
            title='Тестовая новость',
            description='Описание тестовой новости',
            category=category,
            author=user.profile,
        )

    def test_if_main_page_works(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)

    def test_if_main_page_use_right_template(self):
        response = self.client.get(reverse('main_page'))
        self.assertTemplateUsed(response, 'site/main_page.html')

    def test_if_main_page_use_wrong_template(self):
        response = self.client.get(reverse('main_page'))
        self.assertTemplateNotUsed(response, 'site/login.html')

    def test_if_user_can_create_news(self):
        category = NewsCategory.objects.get(category='Спорт')
        user = User.objects.get(username='test1')
        self.client.login(username='test1', password='test1')
        self.client.post(reverse('create_news'), {
            'title': 'Новость 1',
            'description': 'Описание новости 1',
            'category': category.pk,
            'author': user.pk,
        })
        self.assertTrue(News.objects.filter(title='Новость 1').exists())

    def test_if_news_detail_page_works(self):
        news = News.objects.get(title='Тестовая новость')
        response = self.client.get(reverse('news_detail', kwargs={'pk': news.pk}))
        self.assertEqual(response.status_code, 200)

    def test_if_news_detail_page_use_right_template(self):
        news = News.objects.get(title='Тестовая новость')
        response = self.client.get(reverse('news_detail', kwargs={'pk': news.pk}))
        self.assertTemplateUsed(response, 'site/news_detail.html')

    def test_if_news_detail_page_use_wrong_template(self):
        news = News.objects.get(title='Тестовая новость')
        response = self.client.get(reverse('news_detail', kwargs={'pk': news.pk}))
        self.assertTemplateNotUsed(response, 'site/main_page.html')

    def test_if_post_quantity_increase_after_publication(self):
        category = NewsCategory.objects.get(category='Спорт')
        user = User.objects.get(username='test1')
        self.client.login(username='test1', password='test1')
        self.client.post(reverse('create_news'), {
            'title': 'Новость 1',
            'description': 'Описание новости 1',
            'category': category.pk,
            'author': user.pk,
        })
        self.assertEqual(user.profile.news_quantity, 1)

    def test_if_user_can_update_stranger_news(self):
        user = User.objects.create(username='test2')
        user.set_password('test2')
        user.save()
        Profile.objects.create(user=user)
        news = News.objects.get(title='Тестовая новость')
        self.client.login(username='test2', password='test2')
        response = self.client.get(reverse('update_news', kwargs={'pk': news.pk}))
        self.assertEqual(response.status_code, 403)

    def test_if_user_can_post_comment(self):
        self.client.login(username='test1', password='test1')
        self.client.post('/news/1/', {'comment': 'Комментарий 1'})
        self.assertTrue(Comment.objects.filter(comment='Комментарий 1').exists())

    def test_if_anonymous_user_can_post_comment(self):
        response = self.client.post('/news/1/', {'comment': 'Комментарий 1'})
        self.assertTrue(response.status_code, 403)

    def test_if_comment_count_raise_after_post(self):
        user = User.objects.get(username='test1')
        self.client.login(username='test1', password='test1')
        self.client.post('/news/1/', {'comment': 'Комментарий 1'})
        self.assertEqual(user.profile.comment_quantity, 1)
