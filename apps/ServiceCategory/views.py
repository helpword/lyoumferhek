from django.http import JsonResponse
from .models import ServiceCategory

def service_category_list(request):
    categories = list(ServiceCategory.objects.values())
    return JsonResponse(categories, safe=False)
