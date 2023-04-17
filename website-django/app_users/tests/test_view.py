from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_users.models import Profile


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test1')
        user.set_password('test1')
        user.save()
        Profile.objects.create(user=user)

    def test_if_registration_page_works(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)

    def test_if_registration_page_use_right_template(self):
        response = self.client.get(reverse('registration'))
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_if_registration_page_use_wrong_template(self):
        response = self.client.get(reverse('registration'))
        self.assertTemplateNotUsed(response, 'users/login.html')

    def test_if_new_user_can_sign_up(self):
        self.client.post(reverse('registration'), {
            'username': 'testuser',
            'password1': 'mypassword777',
            'password2': 'mypassword777',
        })
        self.assertTrue(Profile.objects.filter(user__username='testuser').exists())

    def test_if_user_can_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'test1',
            'password': 'test1',
        })
        user = User.objects.get(username='test1')
        self.assertRedirects(response, reverse('account', kwargs={'username': user.username}))

    def test_if_user_can_logout(self):
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('main_page'))

