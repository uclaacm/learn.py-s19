from django.http import HttpResponse, JsonResponse

my_html = '''
<!DOCTYPE html>
<html>
    <body>
        <h1> Hello World </h1>
    </body>
</html>
'''

def hello_world(request):
    return HttpResponse(my_html)
 
num_calls = 0

def squared(request, num):
    sq = num * num
    global num_calls 
    num_calls += 1
    json = {
        'answer': sq,
        'count': num_calls
    }
    return JsonResponse(json)

def squaredPage(request):
    with open('templates/index.html', 'r') as f:
        return HttpResponse(f.read())
 
