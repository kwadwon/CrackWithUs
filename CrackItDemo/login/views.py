from django.shortcuts import render


def login_page(request, template_name='login/login.html'):

    return render(request, template_name)
