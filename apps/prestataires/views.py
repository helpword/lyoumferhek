from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Prestataire
from django.shortcuts import render, redirect
from .forms import PrestataireRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from apps.services.models import Service



def load_services(request):
    type_id = request.GET.get('type_id')
    services = Service.objects.filter(service_type_id=type_id).values('id', 'name')
    return JsonResponse({'services': list(services)})



def prestataire_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_prestataire:
            login(request, user)
            return redirect('prestataire_dashboard')  # تأكد أن هذه الصفحة موجودة
        else:
            messages.error(request, 'Adresse e-mail ou mot de passe invalide.')
    return render(request, 'prestataires/login.html')


# def prestataire_register_view(request):
#     form = PrestataireRegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('login')  # أو إلى صفحة success
#     return render(request, 'prestataires/register.html', {'form': form})


# عرض صفحة تفاصيل مقدم خدمة
def prestataire_detail(request, pk):
    prestataire = get_object_or_404(Prestataire, pk=pk)
    return render(request, 'prestataire/prestataire_detail.html', {'prestataire': prestataire})

# عرض لوحة التحكم الخاصة بمقدم الخدمة
@login_required
def prestataire_dashboard(request):
    user = request.user
    if hasattr(user, 'prestataire_profile'):
        prestataire = user.prestataire_profile
        return render(request, 'prestataire/dashboard.html', {'prestataire': prestataire})
    else:
        return render(request, 'errors/unauthorized.html')  # أو أي صفحة خطأ عندك
    


def prestataire_register_view(request):
    if request.method == 'POST':
        form = PrestataireRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            prestataire = form.save()
            login(request, prestataire.user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': reverse('prestataire_dashboard')})
            return redirect('prestataire_dashboard')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                html = render_to_string('prestataires/register.html', {'form': form}, request=request)
                return JsonResponse({'success': False, 'html': html})
    else:
        form = PrestataireRegisterForm()
    
    # تحميل أول مرة (GET)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('prestataires/register.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

    return render(request, 'prestataires/register.html', {'form': form})


def prestataire_register(request):
    if request.method == 'POST':
        form = PrestataireRegisterForm(request.POST)
        if form.is_valid():
            prestataire = form.save(commit=False)
            prestataire.set_password(form.cleaned_data['password'])
            prestataire.save()
            return redirect('login')
    else:
        form = PrestataireRegisterForm()
    return render(request, 'prestataires/register.html', {'form': form})


