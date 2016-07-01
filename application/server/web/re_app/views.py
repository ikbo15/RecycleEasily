import os
from django.conf import settings
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('re_app/ymaps.html')
	return HttpResponse(template.render(request))
