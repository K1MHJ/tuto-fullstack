from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect

import json
import time
import subprocess

@csrf_exempt
def index(request):
    if request.method == "GET":
        return JsonResponse({})
    data = json.loads(request.body)
    print(data["a"])
    print(data["b"])

    my_root = "/Users/hyungjinkim/Developments/web-app/back-end/bin"
    my_exe = my_root + "/" + "hello"
    print(my_exe)
    result = subprocess.run([my_exe],capture_output=True, text=True)
    if result.returncode == 0:
        print("successfully")
    else:
        print("return code:", result.returncode)
    print("Program Print")
    print(result.stdout)
    return JsonResponse({'result': True})

