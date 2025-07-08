from django.http import JsonResponse
from .models import Client
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
