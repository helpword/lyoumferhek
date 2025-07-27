from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from apps.prestataires.models import Prestataire
from django.contrib.auth.decorators import login_required

@login_required
def leave_review(request, prestataire_id):
    prestataire = get_object_or_404(Prestataire, id=prestataire_id)
    client = request.user.client

    if Review.objects.filter(client=client, prestataire=prestataire).exists():
        return redirect('prestataire_detail', prestataire_id=prestataire.id)  # منع التكرار

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = client
            review.prestataire = prestataire
            review.save()
            return redirect('prestataire_detail', prestataire_id=prestataire.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/leave_review.html', {'form': form, 'prestataire': prestataire})
