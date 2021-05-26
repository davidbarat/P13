from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from help.models import Group


class UrlsTest(TestCase):

    def test_mentions(self):
        url = self.client.get(reverse("mentions"))
        self.assertEqual(url.status_code, 200)

    def test_faq(self):
        url = self.client.get(reverse("faq"))
        self.assertEqual(url.status_code, 200)

    def test_about(self):
        url = self.client.get(reverse("about"))
        self.assertEqual(url.status_code, 200)
