from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from bauth.authentication import TokenAuthentication

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context={
        #'description':"Hello, world. You're at the ItalyInformatica project index.",
        'name':"The Italy Informatica Project - Backend",
        }
    return render(request,'reddit/index.html', context)

@login_required
def private(request): 
    context={
        'you':request.user
        }
    return render(request,'reddit/private.html', context)

class AuthenticatedView(APIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    
    # do not put this in the schema
    exclude_from_schema = True
    
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
