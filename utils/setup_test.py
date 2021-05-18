from django.test import TestCase
from authentication.models import User
from faker import Faker


class TestSetup(TestCase):

    def setUp(self):
        # print("Test started")
        self.faker = Faker()
        self.password = self.faker.paragraph(nb_sentences=5)

        self.user = {
            "username" : self.faker.name().split(" ")[0],
            "email" : self.faker.email(),
            "password" : self.password,
            "password2" : self.password,
        }
        # print(self.user["username"])
        # return super().setUp()

    def create_test_user(self):
        user = User.objects.create(username="username", email="email@app.com")
        user.set_password("getyours")
        user.is_email_verified = True
        user.save()
        return user

    def create_test_user_two(self):
        user = User.objects.create(username="username2", email="email2@app.com")
        user.set_password("getyours")
        user.save()
        return user

    def tearDown(self):
        return super().tearDown()