from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.prestataires.models import Prestataire
from apps.wilayas.models import Wilaya, Commune
from apps.clients.models import Client
from .forms import WilayaCommuneForm, Step1Form, Step2Form, Step3Form, Step4Form
from apps.events.models import Reservation
from .models import Service
from apps.services.models import ServiceCategory
from apps.events.models import EventType

def register_prestataire(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'prestataire/register.html', {
        'categories': categories,
        # إذا كنت ترسل فورم أيضاً أضفه هنا
    })


def get_services_by_category(request):
    category_id = request.GET.get('category_id')
    services = Service.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(services), safe=False)



def ajax_load_services(request):
    category_id = request.GET.get('category_id')  # <-- هذا هو الصحيح الآن
    services = Service.objects.filter(category_id=category_id).values('id', 'name_fr', 'name_ar')
    return JsonResponse(list(services), safe=False)



def redirect_to_step1(request):
    return redirect('step1')

def wilaya_commune_test(request):
    form = WilayaCommuneForm()
    return render(request, 'form/wilaya_commune_test.html', {'form': form})

def load_communes(request):
    wilaya_id = request.GET.get('wilaya')
    communes = Commune.objects.filter(wilaya_id=wilaya_id).values('id', 'name')
    return JsonResponse(list(communes), safe=False)

def home(request):
    prestataires = Prestataire.objects.all()
    return render(request, 'services/home.html', {'prestataires': prestataires})

def step1_view(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            request.session['step1'] = form.cleaned_data
            return redirect('step2')
    else:
        form = Step1Form()
    return render(request, 'form/step1.html', {'form': form})

def step2_view(request):
    if request.method == 'POST':
        form = Step2Form(request.POST)
        if form.is_valid():
            request.session['step2'] = form.cleaned_data
            return redirect('step3')
    else:
        form = Step2Form()
    return render(request, 'form/step2.html', {'form': form})

def step3_view(request):
    if request.method == 'POST':
        form = Step3Form(request.POST)
        if form.is_valid():
            request.session['step3'] = form.cleaned_data
            return redirect('step4')
    else:
        form = Step3Form()
    return render(request, 'form/step3.html', {'form': form})

def step4_view(request):
    if request.method == 'POST':
        form = Step4Form(request.POST)
        if form.is_valid():
            request.session['step4'] = form.cleaned_data
            return redirect('form_complete')
    else:
        form = Step4Form()
    return render(request, 'form/step4.html', {'form': form})

def form_complete_view(request):
    data = {
        'step1': request.session.get('step1'),
        'step2': request.session.get('step2'),
        'step3': request.session.get('step3'),
        'step4': request.session.get('step4'),
    }
    return render(request, 'form/complete.html', data)


def service_search_page(request):
    context = {
        "event_types": EventType.objects.all(),
        "categories": ServiceCategory.objects.all(),
        "wilayas": Wilaya.objects.all(),
    }
    return render(request, "services/search_page.html", context)

def home(request):
    user = request.user

    try:
        client = user.client_profile
    except Client.DoesNotExist:
        client = None

    confirmed_reservations = pending_reservations = canceled_reservations = events_count = 0

    if client:
        reservations = Reservation.objects.filter(client=client)
        confirmed_reservations = reservations.filter(status='confirmed').count()
        pending_reservations = reservations.filter(status='pending').count()
        canceled_reservations = reservations.filter(status='canceled').count()
        events_count = reservations.count()

    context = {
        'confirmed_reservations': confirmed_reservations,
        'pending_reservations': pending_reservations,
        'canceled_reservations': canceled_reservations,
        'events_count': events_count,
        # أضف أي متغيرات أخرى تحتاجها في القالب
    }

    return render(request, 'home/index.html', context)

def filter_services(request):
    event_type = request.GET.get("event_type")
    category = request.GET.get("category")
    wilaya = request.GET.get("wilaya")
    commune = request.GET.get("commune")

    services = Service.objects.all()

    if event_type:
        services = services.filter(service_category__event_types__id=event_type)
    if category:
        services = services.filter(service_category_id=category)
    if wilaya:
        services = services.filter(prestataire__commune__wilaya_id=wilaya)
    if commune:
        services = services.filter(prestataire__commune_id=commune)

    return render(request, "services/partials/service_list.html", {"services": services})