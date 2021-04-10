from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.core.exceptions import ValidationError
from .forms import UserForm, RegisterForm, UserProfileForm
from .models import UserProfile

def index(request):
    return HttpResponse("Hello, world. You're at the help index.")

@transaction.atomic
def register(request):
    registered = False
    if request.method == "POST":
        user_form = RegisterForm(data=request.POST)
        userprofile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            phone = userprofile_form.cleaned_data.get("phone")
            userprofile = UserProfile.objects.filter(user_id=user.id)
            userprofile.update(phone=phone)
            registered = True
        else:
            messages.error(request, _('Veuillez corriger les erreurs ci-dessous.'))
    else:
        user_form = RegisterForm()
        userprofile_form = UserProfileForm()
    return render(
        request, "help/registration.html", {
            "user_form": user_form, 
            "userprofile_form":userprofile_form,
            "registered": registered}
    )