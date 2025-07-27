from django.http import JsonResponse
from .models import Commune, Wilaya
from django.http import HttpResponse
from django.template.loader import render_to_string

def wilaya_list(request):
    wilayas = list(Wilaya.objects.values())
    return JsonResponse(wilayas, safe=False)


def commune_list(request):
    communes = list(Commune.objects.values())
    return JsonResponse(communes, safe=False)



def get_communes(request):
    wilaya_id = request.GET.get("wilaya_id")
    communes = Commune.objects.filter(wilaya_id=wilaya_id).values("id", "name_ar")
    return JsonResponse(list(communes), safe=False)