from django.db import models


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
        return super(UserProfileManager, self).filter(
            group_id__exact=group_id).values('phone')


class GroupManager(models.Manager):

    def get_id(self, group_name):
        return super(GroupManager, self).filter(
            group_name__exact=group_name).values('id')
