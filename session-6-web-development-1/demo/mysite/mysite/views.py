from django.http import HttpResponse

# Views are Python functions that take a Web request and return a Web Response- in this case, an HttpResponse object
# that contains the contents of the specified HTML page
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