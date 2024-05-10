from django.shortcuts import render
from django.http import JsonResponse
from Kopma_api.models import Kopma

# Create your views here.
def kopma_list(request):
    kopma = kopma.objects.all() # Complex Data
    kopma_python = list(kopma.values()) # python DS
    return JsonResponse({
        'kopma': kopma_python
    })