from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'description':"Hello, world. You're at the ItalyInformatica project index.",
        }
    return render(request,'root/index.html', context)

