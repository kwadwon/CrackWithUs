# This code and all its derivatives exclusively belongs to crackit inc
# Author: Perry Ogwuche - 8-21-2-2013

from django.shortcuts import render


def login_page(request, template_name='login/login.html'):

    return render(request, template_name)
