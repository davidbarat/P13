from django.shortcuts import render
from help.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def list(request):
    # template = loader.get_template("group/list.html")
    groups = Group.objects.all()
    context = {
            "groups": groups
        }
    return render(request, "group/list.html", context )
    # return HttpResponse(template.render(request=request))