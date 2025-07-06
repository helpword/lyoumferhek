from django.http import JsonResponse
from .models import Wilaya

def wilaya_list(request):
    wilayas = list(Wilaya.objects.values())
    return JsonResponse(wilayas, safe=False)
