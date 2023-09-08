from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('THIS IS HOME PAGE')


def aboutPageView(request):
    return HttpResponse('THIS IS ABOUT PAGE')


def contactPageView(request):
    return HttpResponse('THIS IS CONTACT PAGE')
