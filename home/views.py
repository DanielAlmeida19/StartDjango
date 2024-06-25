# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    print('home do app')
    return HttpResponse('home do app')
