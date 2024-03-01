from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def index(request):
    htm=loader.get_template('index.html')
    return HttpResponse(htm.render())

def insert(request):
    name=request.GET['name']
    print(name)
    htm=loader.get_template('index.html')
    return HttpResponse(htm.render({"name":name}))
