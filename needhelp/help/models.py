from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.group_name


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


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date_event = models.DateField()
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        default=1
    )
    group_name = models.CharField(max_length=30, default='default name group')
    status = models.CharField(max_length=10)
    

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