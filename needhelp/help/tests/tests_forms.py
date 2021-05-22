from django.test import TestCase
from help.forms import RegisterForm, UserForm, GroupForm, ContactForm
from django.contrib.auth.models import User


class FormTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.data = {
            "email": "test@test.te",
            "password": "test123",
            "first_name": "Test",
            "last_name": "test",
            "username": "Tester",
        }

        cls.datagroup = {
            "group_name": "test",
            "adress": "rue du test",
            "zipcode": "75001",
            "city": "Paris"
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
        cls.user2.save()
        # cls.userTest = User.objects.get(id=1)

    def test_valid_RegisterForm(self):

        self.form = RegisterForm(data=self.data)
        self.assertTrue(self.form.is_valid())

    def test_valid_UserForm(self):

        self.formUserForm = UserForm(data=self.data)
        self.assertTrue(self.formUserForm.is_valid())

    def test_valid_GroupForm(self):

        self.formUserForm = GroupForm(data=self.datagroup)
        self.assertTrue(self.formUserForm.is_valid())

    def test_valid_ContactForm(self):

        self.formUserForm = ContactForm(data=self.datacontact)
        self.assertTrue(self.formUserForm.is_valid())
