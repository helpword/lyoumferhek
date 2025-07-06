from django.shortcuts import render, get_object_or_404
from .models import EventItem

def event_item_list(request):
    event_items = EventItem.objects.all()
    return render(request, 'eventitem/event_item_list.html', {'event_items': event_items})
