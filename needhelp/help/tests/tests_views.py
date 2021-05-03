from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from help.models import Group


class UrlsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        Group.objects.create(
            group_name="default",
            adress="rue de la paix",
            zipcode="75001",
            city="Paris",
        )
        self.user = User.objects.create_user(
            username='david', email='david@gmail.com', password='csecret')

    def test_mentions(self):
        url = self.client.get(reverse("mentions"))
        self.assertEqual(url.status_code, 200)
