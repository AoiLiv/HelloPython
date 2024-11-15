from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Friend    
from django.views.generic import ListView, DetailView

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend    
    


"""def helloworld(request):
    return HttpResponse("Hello Django!")

def one_hello(request):
    objects = Friend.objects.all()[0]
    html = f"<p>Hello {objects.name}!</p>"
    return HttpResponse(html)

def list_hello(request):
    objects = Friend.objects.all()
    html = ""
    for i in objects:
        html += f"<p>Hello {i.name}!</p>"
    return HttpResponse(html)"""