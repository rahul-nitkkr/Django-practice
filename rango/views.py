from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "The bold thing that is returned"}
    return render(request , 'rango/index.html' , context_dict)

def about(request):
    return HttpResponse("Rango took me here! <a href='/rango/'>Get me Back!</a>")