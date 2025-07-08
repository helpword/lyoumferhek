from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Prestataire

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
