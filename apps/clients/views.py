from django.http import JsonResponse
from .forms import ClientRegisterForm
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Client

def client_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_client:
            login(request, user)
            return redirect('client_dashboard')
        else:
            messages.error(request, 'Adresse e-mail ou mot de passe invalide.')
    return render(request, 'clients/login.html')


def client_register_view(request):
    form = ClientRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')  # أو إلى صفحة success
    return render(request, 'clients/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

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

@login_required
def client_dashboard(request):
    user = request.user
    if hasattr(user, 'client_profile'):
        client = user.client_profile
        return render(request, 'clients/dashboard.html', {'client': client})
    else:
        return JsonResponse({"error": "Client profile not found"}, status=404)
