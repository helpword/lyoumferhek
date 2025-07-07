from django.http import JsonResponse
from .models import Commune, Wilaya

def wilaya_list(request):
    wilayas = list(Wilaya.objects.values())
    return JsonResponse(wilayas, safe=False)


def commune_list(request):
    communes = list(Commune.objects.values())
    return JsonResponse(communes, safe=False)
