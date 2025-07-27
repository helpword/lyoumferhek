from django.http import JsonResponse
from django.shortcuts import render
from apps.users.forms import AuthenticationForm
from apps.wilayas.models import Wilaya, Commune
from apps.events.models import EventType
from apps.services.models import ServiceCategory

def index(request):
    wilayas = Wilaya.objects.all()
    event_types = EventType.objects.all()
    service_categories = ServiceCategory.objects.all()

    return render(request, "index.html", {
        "wilayas": wilayas,
        "event_types": event_types,
        "service_categories": service_categories,
    })

def home_view(request):
    wilayas = Wilaya.objects.all()
    communes = Commune.objects.all()
    context = {
        'wilayas': wilayas,
        'communes': communes,
        'prestataire_login_form' :  AuthenticationForm
    }
    return render(request, 'home/index.html', context)

def select_event_type(request):
    return render(request, 'home/select_event_type.html')

def select_venue_type(request, event_type):
    return render(request, 'home/select_venue_type.html', {'event_type': event_type})

def get_communes(request):
    wilaya_id = request.GET.get('wilaya_id')
    communes = Commune.objects.filter(wilaya_id=wilaya_id).values('id', 'ar_name', 'name_fr')
    return JsonResponse(list(communes), safe=False)
