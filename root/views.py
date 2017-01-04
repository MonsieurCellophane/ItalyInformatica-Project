from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context={
        #'description':"Hello, world. You're at the ItalyInformatica project index.",
        'name':"The Italy Informatica Project - Backend",
        }
    return render(request,'root/index.html', context)

@login_required
def private(request): 
    context={
        'you':request.user
        }
    return render(request,'root/private.html', context)
    
