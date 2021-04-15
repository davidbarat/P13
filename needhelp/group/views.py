from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from help.models import Group, UserProfile
from help.forms import GroupForm


def list(request):
    groups = Group.objects.all()
    context = {
            "groups": groups
        }
    return render(request, "group/list.html", context )

@login_required()
def create(request):
    if request.method == "POST":
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            user = User.objects.filter(user__username=request.user)
            usergroup = UserProfile.objects.filter(user__username=user)
            group.update()
        else:
            messages.error(request, ('Veuillez corriger les erreurs ci-dessous.'))
    else:
        group_form = GroupForm()
    return render(
        request, "group/creategroup.html", {
            "group_form": group_form, 
            }
    )