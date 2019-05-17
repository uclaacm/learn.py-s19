# Learn.py Session 7 Application of Python: Web Development Part 2

__Location__: Covel 227

__Time__: 6:15 PM - 8:15 PM, 33 May 2019

__Teacher__: Galen Wong

## Resrouces:
Slides: [TODO]()

[ACM Membership Attendance Portal](https://members.uclaacm.com/login)

- Want to dive deep into Web Dev? Check out our Hackschool workshop series!
  - https://github.com/uclaacm/hackschool-f18
- Django Documentation
  -  https://docs.djangoproject.com/en/2.2/

## What we'll be learning today?
- What is RPC
- What is JavaScript?
- What is JSON?
- What is an API?

## Recap
Last time we built a Django server application that serves
different html pages based on the routes. 
Let's revisit it. 
First, we create a new Django application.

```
django-admin startproject myapp
```
And your `myapp/` directory should have the same 
structure as this...

<img src="image/emptyfolder.png" width="200px">

... I mean this
```
├── manage.py
└── myapp
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Create a file named `views.py` under `myapp/myapp/`.
```
├── manage.py
└── myapp
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py (We added this file)
    └── wsgi.py
```

Inside `views.py`, we import a function from Django
named `HttpResponse`, create a string that holds our
html page.
```py
from django.http import HttpResponse

my_html = '''
<!DOCTYPE html>
<html>
    <body>
        <h1> Hello World </h1>
    </body>
</html>
'''
```

Then, we can write a function that returns this simple 
page with `HttpResponse`.
```py
def hello_world(request):
    return HttpResponse(my_html)
```

Finally, we add a route to this function in `urls.py`.
```py
from . import views # remember to import

urlpatterns = [
    path('', views.hello_world),
    path('admin/', admin.site.urls),
]
```

We can start the server with
```
python manage.py runserver
```
If you access `localhost:8000` in your browser, you 
should see the simple HTML page we defined.

You might have noticed that we used a different function
to return a html page this time. Last time, we used 
`render` but we are using `HttpResponse` this time. 
But they do the same thing, except we put the html text 
in a file and pass the file name to `render`, and 
`HttpResponse` simply takes in a string.


### Django Routing Model 
<img src="image/routing.jpg" width="300px">

Django calls the corresponding function based on the 
request URL. It matches the URL one by one with the 
URL pattern defined by us in the list `urlpatterns`.
This is how the routing is done.

When a request comes in with URL `localhost:8000`,
Django extracts whatever is after the domain name,
aka this `localhost:8000` portion. Well, it is an 
empty string. Then, Django compare the suffix 
portion (the empty string here) with each path
in the `urlpattern` list. It matches the first one,
then it calls the corresponding function `hello_world`.

## What is RPC?
RPC stands for Remote Procedure Call. 
- Remote
  - Remote means the operation is on a server
- Procedure
  - This word is just a fancy term for function 

Putting it together, RPC is the action of calling a 
function in the server instead of in your code.

## Examples of RPC 
Well, we just did one! The action of visiting our
"hello world" web page was a RPC. We have use an URL 
`localhost:8000` to access the server with a request and 
the server calls a function `hello_world` for us using 
the routing mechanism. The function returns a string 
which is in the response and the string is displayed on
the browser. If the string is an html page, the browser
renders it with style.

Now we see the server as a blackbox that provides us 
with different functions for us to call.

Let's us build some function that we can call.

```py
# views.py
def squared(request, num):
    sq = num * num
    return HttpResponse(sq)
```
Also add a route to this function
```py
urlpatterns = [
    path('', views.hello_world),
    path('square/<int:num>/', views.squared),
    path('admin/', admin.site.urls),
]
```
Remember from last time. We can match generic number with
the `<int:num>` special string within our URL pattern.
And Django will call our `squared` function with 
parameter `num` set to the value in the URL.

See what happens when you access the "page" 
`localhost:8000/square/2` from your browser.

This is just like calling a function. __We call a 
function on the server with the URL which helps the 
server (Django) to identify which function you want to 
call!__ This is also a RPC.


Now we see that using URL, not only can we request for 
html page, we can also request for data. 
So far we only have 2 types of data. We requested for 
(1) an HTML page, (2) a number/integer. 

## What is JavaScript?
Well, so far our webpages have been static. We can also 
make it more interactive with JavaScript. 
JavaScript is a programming language for the web. __It 
allows you to interact with a HTML page and modify it.__

Let's try it out! First, we create a `index.html` file.
```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<button id="btn">Calculate 2 squared</button>
	<h1>Answer:</h1>
	<h1 id="answer"></h1>
</body>
```
Notice how we have a `id` attribute to the tags `button` 
and `h1`. This attribute allows us to name an element so 
we can tell it apart from the other tags. For example,
`h1 id="answer"` is different from just `h1`. 
We will use it in JavaScript later.

Where do we add our JavaScript then? We can add it inside
a special tag called `script`.

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<script type="text/javascript">
		console.log('welcome to JavaScript');
	</script>
</head>
<body>
	<button id="btn">Calculate 2 squared</button>
	<h1>Answer:</h1>
	<h1 id="answer"></h1>
</body>
</html>
```
`console.log` is the `print` function in JavaScript. 
To see that it got executed, we can go to the Console 
in our browser.
1. Left click on any page. Click `Inspect`.
1. You should see something like this.

<img src="image/devtool.png" width="500px">

If you go to the `Console` Tab, you should see
`welcome to JavaScript` being outputed.

How can we access the HTML element/tags?
We use a built in function called `getElementById`.

```js
// within the <script> tag
function main() {
    var ourButton = document.getElementById('btn');
    var ourAnswer = document.getElementById('answer');
    console.log(ourButton.innerText);
}
window.onload = main;
```
Notice a few things here. 
- `var ourButton` is how we declare a variable in JavaScript
- `getElementById` returns an HTML object
- `ourButton` and `ourAnswer` are objects that refers to our 
  `button` tag and `h2` tags
- `function name() {}` is how we define a function in JavaScript
- we can assign a function to a variable called `window.onload`
    - this tells JavaScript to execute this function when the 
      page finishes loading

We do not have time to cover a lot of JavaScript in this workshop. 
If you are interested, please checkout HackSchool's tutorial on 
JavaScript. 

Reload your `index.html` in your browser to see what happens in 
the Console!

Quite cool! We can see what is inside the `button` tag 
by printing a property within the object of `ourButton`.
Let's serve this page as part of our Django server!

We put this file inside a folder called `templates`.
```
├── db.sqlite3
├── manage.py
├── myapp
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
└── templates (we added this)
    └── index.html
```
We add a function for this page in `views.py`
```py
def squaredPage(request):
    with open('templates/index.html', 'r') as f:
        return HttpResponse(f.read())
```
Remember file handling? We directly here read the html file.
And returning its contents as string!
Now we add a route to this function in `urls.py`
```py
urlpatterns = [
    path('', views.hello_world),
    path('square/<int:num>/', views.squared),
    path('square/', views.squaredPage), # we added this line
    path('admin/', admin.site.urls),
]
```

Try visting `localhost:8000/square` in your browser.
See what happens!


## Request for data in the frontend
Remember the very complicated function that we defined in 
our server? We can make use of it from our website!
Also, by making a request to the server at the given URL. 
We have been making request by typing the URL in our browser.
JavaScript provides a function `fetch` for us to let our 
code make a request to server as well!

```js
function main() {
    var ourButton = document.getElementById('btn');
    var ourAnswer = document.getElementById('answer');
    console.log(ourButton.innerText);
    fetch('http://localhost:8000/square/2').then(function (response) {
        console.log(response);
    })
}
window.onload = main;
```

It prints a sort of convoluted object inside the console.
We should be simply expecting the number `4` in the 
response. It does not seem to be anywhere. 
Turns out we need to get it in another `then` block.
```js
fetch('http://localhost:8000/square/2')
.then(function (response) {
    return response.json();
})
.then(function (json) {
    console.log(json);
})
```

Now we see `4` being printed in our Console!

## Time to Get Interactive