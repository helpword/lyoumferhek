from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.prestataires.models import Prestataire
from django.shortcuts import render, redirect
from .forms import PrestataireRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.urls import reverse
import json
from django.utils.safestring import mark_safe
from apps.orders.models import Order  # حسب مكان Model الحجوزات
from apps.services.models import Service
from apps.reviews.models import Review  # إذا كنت تستخدم تقييمات وتعليقات
from django.utils.timezone import now
from datetime import timedelta
from apps.prestataires.forms import PrestataireUpdateForm
from django.http import Http404




# def prestataire_login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None and user.is_prestataire:
#             login(request, user)
#             return redirect('prestataires:prestataire_dashboard')  # تأكد أن هذه الصفحة موجودة
#         else:
#             messages.error(request, 'Adresse e-mail ou mot de passe invalide.')
#     return render(request, 'prestataires/dashboard.html')


# def prestataire_register_view(request):
#     form = PrestataireRegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('login')  # أو إلى صفحة success
#     return render(request, 'prestataires/register.html', {'form': form})


# عرض صفحة تفاصيل مقدم خدمة
def prestataire_detail(request, pk):
    prestataire = get_object_or_404(Prestataire, pk=pk)
    reviews = Review.objects.filter(prestataire=prestataire)
    average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']

    return render(request, 'prestataire/prestataire_detail.html', {'prestataire': prestataire})

# عرض لوحة التحكم الخاصة بمقدم الخدمة
@login_required
def prestataire_dashboard(request):
    user = request.user

    if hasattr(user, 'prestataire_profile'):
        prestataire = user.prestataire_profile

        commandes = prestataire.orders.all()
        reviews = prestataire.reviews.all()

        total_orders = commandes.count()
        confirmed_orders = commandes.filter(status='confirmed').count()
        pending_orders = commandes.filter(status='pending').count()
        cancelled_orders = commandes.filter(status='cancelled').count()

        latest_orders = commandes.order_by('-date')[:5]
        total_services = Service.objects.filter(prestataire=prestataire).count()
        recent_reviews = Review.objects.filter(prestataire=prestataire).order_by('-created_at')[:3]

        ratings = [review.rating for review in reviews]
        ratings_json = mark_safe(json.dumps(ratings))

        return render(request, 'prestataires/dashboard.html', {
            'prestataire': prestataire,
            'total_orders': total_orders,
            'confirmed_orders': confirmed_orders,
            'pending_orders': pending_orders,
            'cancelled_orders': cancelled_orders,
            'latest_orders': latest_orders,
            'total_services': total_services,
            'recent_reviews': recent_reviews,
            'reviews': reviews,
            'ratings_json': ratings_json,
            'commandes': commandes,
        })

    return redirect('home')




def prestataire_register_view(request):
    if request.method == 'POST':
        form = PrestataireRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # prestataire = Prestataire.objects.create(user=user)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': reverse('prestataires:prestataire_dashboard')})
            return redirect('prestataires:prestataire_dashboard')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                html = render_to_string('prestataires/register.html', {'form': form}, request=request)
                return JsonResponse({'success': False, 'html': html})
    else:
        form = PrestataireRegisterForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('prestataires/register.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

    return render(request, 'prestataires/register.html', {'form': form})





@login_required
def update_profile(request):
    try:
        prestataire = request.user.prestataire_profile
    except Prestataire.DoesNotExist:
        raise Http404("ملف مقدم الخدمة غير موجود")

    if request.method == 'POST':
        form = PrestataireUpdateForm(request.POST, request.FILES, instance=prestataire)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تحديث الملف الشخصي بنجاح.")
            return redirect('prestataires:prestataire_dashboard')
    else:
        form = PrestataireUpdateForm(instance=prestataire)

    return render(request, 'prestataires/update_profile.html', {'form': form})


@login_required
def add_service(request):
    return render(request, 'prestataires/add_service.html')


@login_required
def my_services(request):
    return render(request, 'prestataires/my_services.html')


@login_required
def calendar_view(request):
    return render(request, 'prestataires/calendar.html')


@login_required
def inbox_view(request):
    return render(request, 'prestataires/inbox.html')


@login_required
def update_profile_view(request):
    return render(request, 'prestataires/update_profile.html')