from django.http import JsonResponse
from .models import EventType

def event_type_list(request):
    types = list(EventType.objects.values())
    return JsonResponse(types, safe=False)
