from django.http import HttpResponse

def home_page(request):
    file = open("../../index.html")
    html = file.read()
    return HttpResponse(html)

def dark_mode(request):
    file = open("../../darkMode.html")
    html = file.read()
    return HttpResponse(html)

def piktures(request):
    file = open("../../piktures.html")
    html = file.read()
    return HttpResponse(html)