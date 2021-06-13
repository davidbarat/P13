from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from twilio.rest import Client
from .managers import EventManager, UserProfileManager, GroupManager


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.group_name

    objects = GroupManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        default=1
    )
    phone = PhoneField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    objects = UserProfileManager()


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date_event = models.DateTimeField()
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    group_name = models.CharField(max_length=30, default='default name group')
    status = models.CharField(max_length=10)

    objects = EventManager()

    def save(self, *args, **kwargs):
        """
        groups_data = serializers.serialize(
            "json",
            Group.objects.filter(
                group_name__exact=self.group_name).values('id')[0], fields=("group"),
        )
        """
        group = Group.objects.filter(
            group_name__exact=self.group_name).values('id')[0]
        self.group_id = group["id"]
        # groups_json = json.loads(groups_data)
        """
        for group in groups_json:
            self.group = group["id"]
        """
        super(Event, self).save(*args, **kwargs)

    # def notify_bysms(self):
    # @staticmethod
    def notify_bysms(self, group_name):
        number_list = []
        result_group_id = Group.objects.get_id(group_name)
        for group in result_group_id:
            id_group = group['id']
        number_list = UserProfile.objects.get_number(id_group)
        # print(number_list)
        sid = self.send_message(number_list)
        """
        for i in number_list:
            recipient = '+33'+str(i.phone)
            print(recipient)
            client.messages.create(
                to=recipient,
                from_=settings.TWILIO_NUMBER,
                body=message_to_broadcast)
        # return sent_message.sid
        """
        return sid

    def send_message(self, number_list):
        message_to_broadcast = (
            "J'ai besoin d'aide"
            )
        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN)
        for i in number_list:
            recipient = '+33'+str(i.phone)
            print(recipient)
            sent_message = client.messages.create(
                to=recipient,
                from_=settings.TWILIO_NUMBER,
                body=message_to_broadcast)
        return sent_message.sid


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(email__iexact=username))
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by("id").first()
        except user.DoesNotExist as exc:
            message = str(exc)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None