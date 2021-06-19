from django.template import loader
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from help.models import UserProfile, Event, Group


def index(request):
    template = loader.get_template('help/index.html')
    return HttpResponse(template.render(request=request))


def profile(request, username=None):
    if username:
        post_owner = get_object_or_404(User, username=username)
    else:
        post_owner = request.user
        group_name, phone = UserProfile.objects.get_group_info(post_owner.id)
        if "default" in str(group_name[0]):
            default = True
        else:
            default = False
        # group_name = Group.objects.get_group_name(group_id)
        group_id = Group.objects.get_id(group_name[0])
        for item in group_id:
            groupid = item['id']
        events = Event.objects.filter(group_id__exact=groupid)
        event_list = []
        if events:
            for elem in events:
                event = {
                    "id": elem.id,
                    "date_event": elem.date_event,
                    "status": elem.status
                }
                event_list.append(event)
            context = {
                "post_owner": post_owner,
                "phone": phone,
                "group_name": group_name[0],
                "event_list": event_list,
                "default": default
                }
        else:
            context = {
                "post_owner": post_owner,
                "profile": profile,
                "phone": phone,
                "group_name": group_name[0],
                "default": default
            }
    return render(request, "help/profile.html", context)


"""
def broadcast_sms(request):
    message_to_broadcast = (
        "Have you played the incredible TwilioQuest ?"
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
"""


def mentions(request):
    template = loader.get_template("help/mentions.html")
    return HttpResponse(template.render(request=request))


def about(request):
    template = loader.get_template("help/about.html")
    return HttpResponse(template.render(request=request))


def contact(request):
    template = loader.get_template("help/contact.html")
    return HttpResponse(template.render(request=request))


def faq(request):
    template = loader.get_template('help/faq.html')
    return HttpResponse(template.render(request=request))
