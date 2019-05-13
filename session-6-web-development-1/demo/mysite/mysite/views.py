from django.shortcuts import render, render_to_response

# Views are Python functions that take a request and return a response - in this case, an HttpResponse object
# that contains the contents of the specified HTML page
def home_page(request):
    return render(request, 'index.html')

def dark_mode(request):
    return render(request, 'darkMode.html')
    
def piktures(request, num):
    print('num is equal to',num)
    return render(request, 'piktures.html')