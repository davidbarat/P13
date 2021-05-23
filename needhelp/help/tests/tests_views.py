from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from help.models import Group


class UrlsTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = User.objects.create_user(
            username="test",
            email="test@test.te",
            password="test123",
            last_name="test",
            first_name="Test",
        )
        cls.group = Group(
            group_name='default',
            adress='rue de la paix',
            zipcode='75001',
            city='Paris')

        cls.group.save()
        cls.user.save()

    def test_mentions(self):
        url = self.client.get(reverse("mentions"))
        self.assertEqual(url.status_code, 200)
