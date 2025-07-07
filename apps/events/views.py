from django.http import JsonResponse
from .models import Event

def event_list(request):
    events = list(Event.objects.values())
    return JsonResponse(events, safe=False)

def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        return JsonResponse({
            "id": event.id,
            "event_type": event.event_type.name,
            "client": event.client.id,
            "date": event.date,
        })
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)
