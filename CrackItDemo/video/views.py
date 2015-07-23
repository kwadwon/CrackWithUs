# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import vline

@login_required
def video_page(request, template_name='video/mock.html'):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    if request.user.is_authenticated():
        users = map(vline.create_user_profile, User.objects.all())
    else:
        users = None
    return render_to_response(template_name, {
        "users": users, "username": username,
    }, context_instance=RequestContext(request))


