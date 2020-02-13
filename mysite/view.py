from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>arslan </h1>")

def arslan(request):
    return HttpResponse("<h1>arslan </h1>")