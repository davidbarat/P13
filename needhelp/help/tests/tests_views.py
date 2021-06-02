from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from help.models import Group, Event
from datetime import datetime


class UrlsTest(TestCase):

    def setUp(self):
        self.now = datetime.now()
        self.dt_formated = self.now.strftime("%Y-%m-%dT%H:%M:%S")
        self.first_name = 'testuser'
        self.last_name = 'testname'
        self.phone = '0101010101'
        self.email = 'testuser@gmail.com'
        self.username = 'testuser@gmail.com'
        self.password = 'password1234'

        self.group_name = 'testgroup_name'
        self.adress = "rue de la paix"
        self.zipcode = "75001"
        self.city = "Paris"

        self.group = Group(
            group_name='default',
            adress='rue de la paix',
            zipcode='75001',
            city='Paris')

        self.group.save()

        self.event = Event(
            group_name='default',
            date_event=self.dt_formated,
            status='open')

        self.event.save()

    def test_mentions(self):
        url = self.client.get(reverse("mentions"))
        self.assertEqual(url.status_code, 200)

    def test_faq(self):
        url = self.client.get(reverse("faq"))
        self.assertEqual(url.status_code, 200)

    def test_about(self):
        url = self.client.get(reverse("about"))
        self.assertEqual(url.status_code, 200)

    def test_logout2(self):
        url = self.client.get(reverse("index"))
        self.assertEqual(url.status_code, 200)

    def test_register(self):
        response = self.client.post(reverse('register'), data={
            'first_name': self.first_name,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        event = Event.objects.filter(group_name='default')
        event.update(status="closed")
        event_status = Event.objects.filter(
            group_name='default').values('status')
        for elem in event_status:
            status = elem["status"]

        self.assertEqual(status, "closed")

    def test_create(self):
        response = self.client.post(reverse('creategroup'), data={
            'group_name': self.group_name,
            'adress': self.adress,
            'zipcode': self.zipcode,
            'city': self.city
        })
        self.assertEqual(response.status_code, 200)
