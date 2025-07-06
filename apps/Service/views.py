from django.http import JsonResponse
from .models import Service

def service_list(request):
    services = list(Service.objects.values())
    return JsonResponse(services, safe=False)
