from django.db import models
# from .models import Group


class EventManager(models.Manager):

    def create(self, date_event, group_name, status):
        event = self.model(
            date_event=date_event,
            group_name=group_name,
            status=status)
        event.save()
        event.notify_bysms(group_name)
        return event


class UserProfileManager(models.Manager):

    def get_number(self, group_id):
        number_list = []
        number_list = super(
            UserProfileManager,
            self).filter(group_id__exact=group_id)
        return(number_list)

    def get_group_info(self, user_id):
        profiles = super(UserProfileManager, self).filter(
            id__exact=user_id)
        for elem in profiles:
            group_name = elem.group,
            phone = elem.phone
        print(group_name)
        print(phone)
        return(group_name, phone)


class GroupManager(models.Manager):

    def get_id(self, group_name):
        return super(GroupManager, self).filter(
            group_name__exact=group_name).values('id')

    def get_group_name(self, group_id):
        return super(GroupManager, self).filter(
            id__exact=group_id).values('group_name')
