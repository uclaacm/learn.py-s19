from django.shortcuts import render

# Views are Python functions that take a Web request and return a Web Response- in this case, an HttpResponse object
# that contains the contents of the specified HTML page
def home_page(request):
    return render(request, 'index.html')

def dark_mode(request):
    return render(request, 'darkMode.html')
    
def piktures(request):
    return render(request, 'piktures.html')