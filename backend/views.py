from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def login(request):
    if request.method == 'GET':
        return JsonResponse({'foo1': 'bar1'})
    elif request.method == 'POST':
        return JsonResponse({'foo2': 'bar2'})