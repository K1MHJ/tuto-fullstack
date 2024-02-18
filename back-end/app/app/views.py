from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
import json
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden

@csrf_protect
def CsrfView(request):
    print("=======CSRF VIEW=====================")
    csrf = get_token(request)
    print(csrf)
    return JsonResponse({'token': csrf})

@csrf_exempt
def PingView(request):
    if request.method == 'POST':
        # Manually check CSRF token
        if not request.POST.get('csrfmiddlewaretoken') == request.META.get('CSRF_COOKIE'):
            return JsonResponse({'result': 'CSRF token validation failed'})
        # Handle the POST request
    # Handle other HTTP methods
    else:
        print('GET')
    return JsonResponse({'result': True})

def test(request):
    print("==============POST received================")
    return JsonResponse({})

