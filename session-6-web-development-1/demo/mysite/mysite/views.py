from django.shortcuts import render, render_to_response
# Views are Python functions that take a Web request and return a Web Response- in this case, an HttpResponse object
# that contains the contents of the specified HTML page
def home_page(request):
    return render(request, 'index.html')

def dark_mode(request):
    return render(request, 'darkMode.html')
    
def piktures(request, num=-1):
    if (num == -1):
        return render(request, 'piktures.html')
    else:
        return render(request, 'piktures/1.html')

def piktures_home(request):
    print('hallo')
    #return render(request, 'piktures.html')
    return render_to_response('piktures_home.html')