# Create your views here.

from django.shortcuts import render

def video_page(request, template_name='video/mock.html'):
	return render(request, template_name)
