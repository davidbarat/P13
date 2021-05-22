from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import transaction
from django.template import loader
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from .forms import UserForm, RegisterForm, UserProfileForm, ContactForm
from .models import UserProfile, Event


def index(request):
    template = loader.get_template("help/index.html")
    return HttpResponse(template.render(request=request))


@transaction.atomic
def register(request):
    registered = False
    if request.method == "POST":
        user_form = RegisterForm(data=request.POST)
        userprofile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            phone = userprofile_form.cleaned_data.get("phone")
            userprofile = UserProfile.objects.filter(user_id=user.id)
            userprofile.update(phone=phone)
            registered = True
        else:
            messages.error(request, (
                'Veuillez corriger les erreurs ci-dessous.'))
    else:
        user_form = RegisterForm()
        userprofile_form = UserProfileForm()
    return render(
        request, "help/registration.html", {
            "user_form": user_form, 
            "userprofile_form": userprofile_form,
            "registered": registered}
    )


def logout2(request):
    logout(request)
    return redirect(reverse("index"))


@login_required()
def update_event(request):
    if request.method == "POST":
        id = request.POST['event_id']
        event = Event.objects.filter(id=id)
        event.update(status="closed")

        return redirect(reverse('profile'))

    else:
        user_form = RegisterForm()
        userprofile_form = UserProfileForm()
    return render(request, "help/profile.html")


def contact(request):
    if request.method == "POST":
        subject = "demande d'info"
        body = {
            'name': request.POST['Nom'],
            'email': request.POST['Email'],
            'phone': request.POST['Mobile'],
            'message': request.POST['Message'],
            }
        message = "\n".join(body.values())

        try:
            send_mail(
                subject,
                message,
                'dav.barat@gmail.com',
                ['dav.barat@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect(reverse('contact'))
    else:
        contact_form = ContactForm()

    return render(request, "help/contact.html", {'contact_form': contact_form})


