from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index( request ):
    return HttpResponse( "Hello" )

def lalo( request ):
    return HttpResponse( "Hola Lalo" )

def juan( request ):
    return HttpResponse( 'Hola Juan' )

def pablo( request ):
    return HttpResponse( 'Hola Pablo' )