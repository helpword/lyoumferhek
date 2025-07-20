from django.http import JsonResponse
from .forms import ClientRegisterForm
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Client
from django.shortcuts import render
from apps.services.models import Service, ServiceCategory
from apps.wilayas.models import Wilaya, Commune
from apps.events.models import Reservation  # أو المسار الصحيح للموديل
from django.contrib.auth import logout

# @login_required
# def client_dashboard(request):
#     user = request.user
#     try:
#         client = user.client_profile
#     except Client.DoesNotExist:
#         return JsonResponse({'error': 'Client profile not found'}, status=404)

#     reservations = Reservation.objects.filter(client=client).select_related('event_type', 'commune')

#     return render(request, 'client/dashboard.html', {
#         'client': client,
#         'reservations': reservations
#     })


def client_list(request):
    clients = list(Client.objects.values())
    return JsonResponse(clients, safe=False)

def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        return JsonResponse({
            "id": client.id,
            "name": client.user.get_full_name(),
            "email": client.user.email,
        })
    except Client.DoesNotExist:
        return JsonResponse({"error": "Client not found"}, status=404)


    

def client_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and hasattr(user, 'client_profile'):
            login(request, user)
            return redirect('client_dashboard')
        else:
            messages.error(request, 'Adresse e-mail ou mot de passe invalide.')
    return redirect('home')



def client_register_view(request):
    form = ClientRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()  # يحفظ المستخدم
        # Client.objects.create(user=user, phone=user.phone)  # ينشئ ملف Client
        if request.user.is_authenticated:
            logout(request)  # تسجيل الخروج إن كان المستخدم مسجلاً دخول مسبقاً
            messages.success(request, 'Vous êtes déjà connecté. Votre profil client a été créé.')
        # login(request, user)  # تسجيل دخول مباشرة إن أردت
        return redirect('client_dashboard')  # أو أي صفحة نجاح
    return render(request, 'clients/register.html', {'form': form})


def search_services(request):
    wilayas = Wilaya.objects.all()
    communes = Commune.objects.all()
    categories = ServiceCategory.objects.all()

    services = Service.objects.all()

    wilaya_id = request.GET.get('wilaya')
    commune_id = request.GET.get('commune')
    category_id = request.GET.get('category')

    if wilaya_id:
        services = services.filter(commune__wilaya_id=wilaya_id)
        communes = Commune.objects.filter(wilaya_id=wilaya_id)  # لتحديث القائمة
    if commune_id:
        services = services.filter(commune_id=commune_id)
    if category_id:
        services = services.filter(category_id=category_id)

    return render(request, 'client/search.html', {
        'wilayas': wilayas,
        'communes': communes,
        'categories': categories,
        'services': services
    })


def client_dashboard(request):
    user = request.user
    
    try:
        client = user.client_profile
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Client profile not found'}, status=404)
# apps/clients/templates/clients/dashboard.html
    # تابع العرض عادي هنا
    return render(request, 'clients/dashboard.html', {'client': client})    