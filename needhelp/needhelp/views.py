from django.template import loader
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from help.models import UserProfile


def index(request):
    template = loader.get_template('help/index.html')
    return HttpResponse(template.render(request=request))

def profile(request, username=None):
    if username:
        post_owner = get_object_or_404(User, username=username)
    else:
        post_owner = request.user
        profiles = UserProfile.objects.filter(id__exact=post_owner.id)
        for profile in profiles:
            {
                "group_name" : profile.group,
                "phone" : profile.phone
            }
        context = {
            "post_owner": post_owner,
            "profile": profile,
        }
    return render(request, "help/profile.html", context)

def broadcast_sms(request):
    message_to_broadcast = (
        "Have you played the incredible TwilioQuest " "yet? Grab it here: https://www.twilio.com/quest"
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