from django.shortcuts import render
from django.http import HttpResponse

def a(requast):
    return HttpResponse("salom")
def b(requast):
    return HttpResponse("hi")
def c(requast):
    return HttpResponse("namaste")

