from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # pull data from database
    # transform
    # send email

    # template to return HTML content to client
    # use render function to render template
    # 2nd parameter is the template
    return render(request, 'hello.html', {'name': 'Cyrus'})


