from django.http import JsonResponse
from .models import Commune

def commune_list(request):
    communes = list(Commune.objects.values())
    return JsonResponse(communes, safe=False)
