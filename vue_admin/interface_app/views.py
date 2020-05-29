from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['POST'])
def loginAction(request):
    return JsonResponse({
        "name":'jack',
        "age":18
    })