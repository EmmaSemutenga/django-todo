from logging import error
from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup

class TestViews(TestSetup):

    def test_should_register_page(self):
        response = self.client.get(reverse('authentication:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_should_show_login_page(self):
        response = self.client.get(reverse('authentication:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_should_signup_user(self):
        response = self.client.post(reverse('authentication:register'), self.user)
        self.assertEquals(response.status_code, 302)

    def test_should_not_signup_user_with_taken_username(self):
        self.client.post(reverse('authentication:register'), self.user)
        response = self.client.post(reverse('authentication:register'), self.user)
        self.assertEqual(response.status_code, 409)

        storage = get_messages(response.wsgi_request)

        # errors = []

        # for message in storage:
        #     print(message)
        #     errors.append(message.message)

        # print(errors)

        self.assertIn("Username is taken, choose another one", list(map(lambda x: x.message, storage)))

        # import pdb #helps put break points in our code
        # pdb.set_trace()

    def test_should_not_signup_user_with_taken_email(self):
        self.user = {
            "username" : "username111",
            "email" : "email@email.com",
            "password" : "password",
            "password2" : "password",
        }

        self.user2 = {
            "username" : "username122",
            "email" : "email@email.com",
            "password" : "password",
            "password2" : "password",
        }
        self.client.post(reverse('authentication:register'), self.user)
        response = self.client.post(reverse('authentication:register'), self.user2)
        self.assertEqual(response.status_code, 409)

    def test_should_login_successfully(self):
        user = self.create_test_user()
        response = self.client.post(reverse('authentication:login'), {'username' : user.username, 'password' : 'getyours'})
        self.assertEquals(response.status_code, 302)

        storage = get_messages(response.wsgi_request)

        self.assertIn(f"Welcome {user.username}", list(map(lambda x: x.message, storage)))

    def test_should_not_login_with_invalid_password(self):
        user = self.create_test_user()
        response = self.client.post(reverse('authentication:login'), {'username' : user.username, 'password' : 'passo1234!'})
        self.assertEquals(response.status_code, 401)


        storage = get_messages(response.wsgi_request)

        self.assertIn("Invalid credentials, try again", list(map(lambda x: x.message, storage)))