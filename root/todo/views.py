from django.http import HttpResponse


def app(request):
    return HttpResponse('ToDo')


