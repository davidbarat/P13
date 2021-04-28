from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from help.models import Group, UserProfile
from help.forms import GroupForm


def list(request):
    # groups = Group.objects.all()
    groups = Group.objects.exclude(group_name__contains='default')
    context = {
            "groups": groups
        }
    return render(request, "group/list.html", context)


@transaction.atomic
@login_required()
def create(request):
    registered = False
    if request.method == "POST":
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            # group = group_form.save()
            group_form.save()
            # user = User.objects.filter(username=request.user)
            # userprofile = UserProfile.objects.filter(user__exact=user[0])
            # userprofile.update(group=group)
            registered = True
        else:
            messages.error(
                request, ('Veuillez corriger les erreurs ci-dessous.'))
    else:
        group_form = GroupForm()
    return render(
        request, "group/creategroup.html", {
            "group_form": group_form,
            "registered": registered
            }
    )


@login_required()
def update_group(request):
    if request.method == "POST":
        groupname = request.POST['inputGroupSelect01']
        user = User.objects.filter(username=request.user)
        userprofile = UserProfile.objects.filter(user__exact=user[0])
        groupid = Group.objects.filter(
            group_name__exact=groupname).values('id')
        userprofile.update(group=groupid)
        return render(request, "help/profile.html")
