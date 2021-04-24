from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from help.models import Event


@receiver(post_save, sender=Event)
def signal_receiver(sender, created, **kwargs):
    if kwargs.get('created', False):
        message_to_broadcast = (
            "J'ai besoin d'aide"
            )
        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN)
        for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
            if recipient:
                client.messages.create(to=recipient,
                                       from_=settings.TWILIO_NUMBER,
                                       body=message_to_broadcast)
        return HttpResponse("messages sent!", 200)