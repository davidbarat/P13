from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import make_aware
from django.conf import settings
from django.contrib.auth.models import User
from help.models import Group, Event, UserProfile
from datetime import datetime
from django.utils.timezone import get_current_timezone


class UrlsTest(TestCase):
    def setUp(self):
        # settings.TIME_ZONE
        # cls.now = datetime.now()
        self.client = Client()
        self.date = datetime.strptime(
            "2021-07-16T22:24:00", "%Y-%m-%dT%H:%M:%S")
        # self.aware_now = make_aware(self.now)
        # self.aware_now.tzinfo
        # cls.dt_formated = cls.now.strftime("%Y-%m-%dT%H:%M:%S")
        self.first_name = 'testuser'
        self.last_name = 'testname'
        self.phone = '0101010101'
        self.email = 'test@test.te'
        self.username = 'test'
        self.password = 'test1234'

        self.group_name = 'testgroup_name'
        self.adress = "rue de la paix"
        self.zipcode = "75001"
        self.city = "Paris"

        self.group = Group(
            group_name='test',
            id='1',
            adress='rue de la paix',
            zipcode='75001',
            city='Paris')

        self.group.save()

        self.group_update = Group(
            group_name='test_update',
            id=2,
            adress='rue de la guerre',
            zipcode='75002',
            city='Paris')

        self.group_update.save()

        self.event = Event(
            group_name='test',
            date_event=self.date,
            status='open')

        self.event.save()

        self.user2 = User.objects.create_user(
            id=1,
            username="test",
            email="test@test.te",
            password="test1234",
            last_name="test",
            first_name="Test",
        )

        self.user2.save()

        self.user = User.objects.get(email=self.email)

        self.userprofile = UserProfile.objects.update(
            user=self.user,
            phone="0607080910"
        )
        self.group_name_update_id = 2

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
        event = Event.objects.filter(group_name='test')
        event.update(status="closed")
        event_status = Event.objects.filter(
            group_name='test').values('status')
        for elem in event_status:
            status = elem["status"]

        self.assertEqual(status, "closed")

    def test_create(self):
        response = self.client.post(
            '/accounts/',
            {'username': self.email, 'password': self.password}
            )
        self.assertTrue(response)

        response = self.client.post('/group/create/', {
            'group_name': self.group_name,
            'adress': self.adress,
            'zipcode': self.zipcode,
            'city': self.city
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_update_group(self):
        response = self.client.post(
            '/accounts/',
            {'username': self.email, 'password': self.password}
            )
        self.assertTrue(response)

        user = User.objects.filter(username=self.user)
        userprofile = UserProfile.objects.filter(user__exact=user[0])
        groupid = Group.objects.filter(
            id__exact=self.group_name_update_id).values('id')
        userprofile.update(group=groupid)
        groupid_updated = Group.objects.filter(
            id__exact=self.group_name_update_id).values('id')
        for item in groupid_updated:
            groupid_new = item['id']
        self.assertEqual(groupid_new, 2)
