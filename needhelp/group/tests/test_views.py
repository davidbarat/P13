from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
from help.models import Group, User, UserProfile, Event


class ViewsTest(TestCase):
    def setUp(self):
        self.first_name = 'testuser'
        self.last_name = 'testname'
        self.phone = '0101010101'
        self.email = 'test@test.te'
        self.username = 'test'
        self.password = 'password1234'
        self.group_name = 'testgroup_name'
        self.adress = "rue de la paix"
        self.zipcode = "75001"
        self.city = "Paris"

        self.group = Group(
                group_name='test2',
                id='2',
                adress='rue de la paix',
                zipcode='75001',
                city='Paris')

        self.group.save()
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

        self.group_name_update = 'testupdate'
        self.group_name_update_id = 2

        self.user = User.objects.get(email=self.email)

        self.userprofile = UserProfile.objects.update(
            user=self.user,
            phone="0607080910"
        )

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
