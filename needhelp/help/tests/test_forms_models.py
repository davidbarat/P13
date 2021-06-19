from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from unittest.mock import Mock, patch
from unittest import mock
from twilio.rest import Client
from help.models import Group, Event, UserProfile
from help.forms import RegisterForm, UserForm, GroupForm, ContactForm
from help.models import GroupManager, EventManager, UserProfileManager


class FormModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.data = {
            "email": "test@test.te",
            "password": "test123",
            "first_name": "Test",
            "last_name": "test",
            "username": "Tester",
        }

        cls.datacontact = {
            "Nom": "Test",
            "Email": "test@test.com",
            "Mobile": "0906070805",
            "Message": "J'ai besoin d'infos"
        }

        cls.user2 = User.objects.create_user(
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
        cls.user2.save()

        cls.user = User.objects.get(pk=1)

        cls.userprofile = UserProfile.objects.update(
            user=cls.user,
            phone="0607080910"
        )

        # cls.userprofile.save()

        cls.group_name = 'default'
        cls.idgroup = 1
        cls.iduser = 1
        cls.phonenumber = "0607080910"

    def test_valid_RegisterForm(self):

        self.form = RegisterForm(data=self.data)
        self.assertTrue(self.form.is_valid())

    def test_valid_UserForm(self):

        self.UserForm = UserForm(data=self.data)
        self.assertTrue(self.UserForm.is_valid())
    """
    def test_valid_GroupForm(self):

        self.GroupForm = GroupForm(data=self.group)
        self.assertTrue(self.GroupForm.is_valid())
    """
    def test_valid_ContactForm(self):

        self.ContactForm = ContactForm(data=self.datacontact)
        self.assertTrue(self.ContactForm.is_valid())

    def test_get_id(self):
        group_id = Group.objects.get_id(self.group_name)
        for item in group_id:
            groupid = item['id']
        self.assertEquals(groupid, self.idgroup)

    def test_get_group_name(self):
        group_name = Group.objects.get_group_name(self.idgroup)
        for item in group_name:
            groupname = item['group_name']
        self.assertEquals(groupname, self.group_name)

    def test_get_group_info(self):
        profiles = UserProfile.objects.get_group_info(self.iduser)
        for elem in profiles:
            phone = elem
        self.assertEquals(phone, self.phonenumber)

    def test_get_number(self):
        number_list = []
        number_list = UserProfile.objects.get_number(self.idgroup)
        for item in number_list:
            phonenumber = str(item.phone)
        self.assertEquals(phonenumber, self.phonenumber)

    """
    @mock.patch('.Event.send_message.messages.create')
    def test_send_message(self, mocked_instance):
        mocked_instance = mocked_instance.return_value
        expected_sid = 'SM87105da94bff44b999e4e6eb90d8eb6a'
        mocked_instance.send_message.return_value.sid = expected_sid
        evt = Event()
        # create_message_mock.return_value.sid = expected_sid
        to = "+33660645522"
        sid = evt.send_message(to)
        
        sent_message = client.messages.create(
                to=to,
                from_=from_,
                body=message_to_broadcast)
        
        # assert create_message_mock.called is True
        # assert sid == expected_sid
    """
