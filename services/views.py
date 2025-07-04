from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Prestataire
from .forms import Step1Form, Step2Form, Step3Form, Step4Form
from django.http import JsonResponse
from .forms import WilayaCommuneForm
from services.models import Commune

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

def load_communes(request):
    wilaya_id = request.GET.get('wilaya')
    communes = Commune.objects.filter(wilaya_id=wilaya_id).values('id', 'name')
    return JsonResponse(list(communes), safe=False)
