from django.shortcuts import redirect, render

def home_view(request):
    return render(request, 'home/index.html')

def select_event_type(request):
    return render(request, 'home/select_event_type.html')

def select_venue_type(request, event_type):
    return render(request, 'home/select_venue_type.html', {'event_type': event_type})
