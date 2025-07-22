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
from apps.events.models import Event, Reservation  # أو المسار الصحيح للموديل
from django.contrib.auth import logout
from django.template.loader import render_to_string







@login_required(login_url='home')
def client_dashboard(request):
    user = request.user

    # التأكد من أن للمستخدم ملف عميل
    if not hasattr(user, 'client_profile'):
         messages.error(request, "Votre profil client est introuvable.")
         return redirect('home')  # أو يمكنك توجيهه لصفحة إنشاء ملف عميل
    client = user.client_profile
    # reservations = Reservation.objects.filter(client=client)

#     confirmed_reservations = reservations.filter(status='confirmed').count()
#     pending_reservations = reservations.filter(status='pending').count()
#     canceled_reservations = reservations.filter(status='canceled').count()
#     events_count = reservations.count()

#     filter_value = request.GET.get('filter')
#     if filter_value == 'confirmed':
#         reservations = reservations.filter(status='confirmed')
#     elif filter_value == 'pending':
#         reservations = reservations.filter(status='pending')
#     elif filter_value == 'canceled':
#         reservations = reservations.filter(status='canceled')

#     context = {
#         'client': client,
#         'reservations': reservations,
#         'confirmed_count': confirmed_reservations,
#         'pending_count': pending_reservations,
#         'canceled_count': canceled_reservations,
#         'events_count': events_count,
#     }

#     return render(request, 'clients/dashboard.html', context)



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



# def client_register_view(request):
#     form = ClientRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save()  # يحفظ المستخدم
#         # Client.objects.create(user=user, phone=user.phone)  # ينشئ ملف Client
#         login(request, user)

#         messages.success(request, "Bienvenue ! Votre compte a été créé.")
#         return redirect('client_dashboard')

#     return render(request, 'clients/register.html', {'form': form})

def client_register_view(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # تأكد من أنك أنشأت client تلقائياً داخل form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # مهم جداً عند وجود أكثر من backend
            login(request, user)

            messages.success(request, "Bienvenue ! Votre compte a été créé.")
            return redirect('client_dashboard')
    else:
        form = ClientRegisterForm()

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


# def client_dashboard(request):
#     user = request.user
#     reservations = Reservation.objects.filter(client=user)
#     confirmed_reservations = reservations.filter(status='confirmed').count()
#     filter_value = request.GET.get('filter')
#     if filter_value == 'confirmed':
#         reservations = reservations.filter(status='confirmed')
#     elif filter_value == 'pending':
#         reservations = reservations.filter(status='pending')

#     context = {
#         'reservations': reservations,
#         'confirmed_reservations': confirmed_reservations,
#     }
#     return render(request, 'clients/dashboard.html', context)


def client_dashboard(request):
    user = request.user

    try:
        client = user.client_profile
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Client profile not found'}, status=404)

    # كل الحجوزات لهذا العميل
    reservations = Reservation.objects.filter(client=client)

    # عدد كل حالة
    confirmed_reservations = reservations.filter(status='confirmed').count()
    pending_reservations = reservations.filter(status='pending').count()
    canceled_reservations = reservations.filter(status='canceled').count()
    events_count = reservations.count()

    # تصفية حسب الفلتر إن وجد
    filter_value = request.GET.get('filter')
    if filter_value == 'confirmed':
        reservations = reservations.filter(status='confirmed')
    elif filter_value == 'pending':
        reservations = reservations.filter(status='pending')
    elif filter_value == 'canceled':
        reservations = reservations.filter(status='canceled')

    context = {
        'client': client,
        'reservations': reservations,
        'confirmed_count': confirmed_reservations,
        'pending_count': pending_reservations,
        'canceled_count': canceled_reservations,
        'events_count': events_count,
    }

    return render(request, 'clients/dashboard.html', context)







# from django.http import JsonResponse
# from .forms import ClientRegisterForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .models import Client
# from apps.services.models import Service, ServiceCategory
# from apps.wilayas.models import Wilaya, Commune
# from apps.events.models import Reservation


# @login_required(login_url='home')
# def client_dashboard(request):
#     user = request.user

#     if not hasattr(user, 'client_profile'):
#         messages.error(request, "Votre profil client est introuvable.")
#         return redirect('home')

#     client = user.client_profile
#     reservations = Reservation.objects.filter(client=client)

#     confirmed_reservations = reservations.filter(status='confirmed').count()
#     pending_reservations = reservations.filter(status='pending').count()
#     canceled_reservations = reservations.filter(status='canceled').count()
#     events_count = reservations.count()

#     filter_value = request.GET.get('filter')
#     if filter_value == 'confirmed':
#         reservations = reservations.filter(status='confirmed')
#     elif filter_value == 'pending':
#         reservations = reservations.filter(status='pending')
#     elif filter_value == 'canceled':
#         reservations = reservations.filter(status='canceled')

#     context = {
#         'client': client,
#         'reservations': reservations,
#         'confirmed_count': confirmed_reservations,
#         'pending_count': pending_reservations,
#         'canceled_count': canceled_reservations,
#         'events_count': events_count,
#     }

#     return render(request, 'clients/dashboard.html', context)


# def client_register_view(request):
#     if request.method == 'POST':
#         form = ClientRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.backend = 'django.contrib.auth.backends.ModelBackend'
#             login(request, user)
#             messages.success(request, "Bienvenue ! Votre compte a été créé.")
#             return redirect('client_dashboard')
#     else:
#         form = ClientRegisterForm()

#     return render(request, 'clients/register.html', {'form': form})


# def client_login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)
#         if user is not None and hasattr(user, 'client_profile'):
#             login(request, user)
#             return redirect('client_dashboard')
#         else:
#             messages.error(request, 'Adresse e-mail ou mot de passe invalide.')
#     return redirect('home')


# def client_list(request):
#     clients = list(Client.objects.values())
#     return JsonResponse(clients, safe=False)


# def client_detail(request, pk):
#     try:
#         client = Client.objects.get(pk=pk)
#         return JsonResponse({
#             "id": client.id,
#             "name": client.user.get_full_name(),
#             "email": client.user.email,
#         })
#     except Client.DoesNotExist:
#         return JsonResponse({"error": "Client not found"}, status=404)


# def search_services(request):
#     wilayas = Wilaya.objects.all()
#     communes = Commune.objects.all()
#     categories = ServiceCategory.objects.all()
#     services = Service.objects.all()

#     wilaya_id = request.GET.get('wilaya')
#     commune_id = request.GET.get('commune')
#     category_id = request.GET.get('category')

#     if wilaya_id:
#         services = services.filter(commune__wilaya_id=wilaya_id)
#         communes = Commune.objects.filter(wilaya_id=wilaya_id)
#     if commune_id:
#         services = services.filter(commune_id=commune_id)
#     if category_id:
#         services = services.filter(category_id=category_id)

#     return render(request, 'client/search.html', {
#         'wilayas': wilayas,
#         'communes': communes,
#         'categories': categories,
#         'services': services
#     })
