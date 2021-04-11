from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    template = loader.get_template('help/index.html')
    return HttpResponse(template.render(request=request))

def profile(request, username=None):
    if username:
        post_owner = get_object_or_404(User, username=username)
    else:
        post_owner = request.user
    args1 = {
        "post_owner": post_owner,
    }
    return render(request, "help/profile.html", args1)