from django.http import HttpResponse

def index(request):
	return HttpResponse("There is RecycleEasily web-application. ")
