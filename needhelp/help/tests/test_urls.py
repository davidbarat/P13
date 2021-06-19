from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User


class UrlsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(
        #     username='david', email='david@gmail.com', password='csecret')

    def test_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
