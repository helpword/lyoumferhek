from django.http import JsonResponse
from .models import Client

def client_list(request):
    clients = list(Client.objects.values())
    return JsonResponse(clients, safe=False)

def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        return JsonResponse({
            "id": client.id,
            "name": client.name,
            "email": client.email,
        })
    except Client.DoesNotExist:
        return JsonResponse({"error": "Client not found"}, status=404)
