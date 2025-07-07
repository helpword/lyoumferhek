from django.shortcuts import render, get_object_or_404
from .models import Prestataire

def prestataire_detail(request, pk):
    prestataire = get_object_or_404(Prestataire, pk=pk)
    return render(request, 'prestataire/prestataire_detail.html', {'prestataire': prestataire})
