from django.db import models


class EventManager(models.Manager):

    def create(self, date_event, group_name, status):
        # group = Group.objects.filter(
        #     group_name__exact=group_name).values('id')
        event = self.model(
            date_event=date_event,
            group_name=group_name,
            status=status)
        event.save()
        event.notify_bysms()
        return event
