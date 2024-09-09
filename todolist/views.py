from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello! It is my apdate fist app!')
