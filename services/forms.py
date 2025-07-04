# forms.py
from django import forms
from .models import Prestataire, Client  # أزل TypeService و Reservation


EVENT_CHOICES = [
    ('mariage', 'Mariage'),
    ('fiancailles', 'Fiançailles'),
    ('anniversaire', 'Anniversaire'),
    ('nouveau_ne', 'Nouveau-né'),
]

WILAYA_CHOICES = [
    ('alger', 'Alger'),
    ('oran', 'Oran'),
    ('constantine', 'Constantine'),
]

VENUE_CHOICES = [
    ('salle', 'Salle'),
    ('hotel', 'Hôtel'),
    ('villa', 'Villa'),
]

SERVICE_CHOICES = [
    ('photographe', 'Photographe'),
    ('traiteur', 'Traiteur'),
    ('musique', 'Musique'),
    ('decoration', 'Décoration'),
]

class Step1Form(forms.Form):
    evenement = forms.ChoiceField(choices=EVENT_CHOICES, label="Type d'événement")

class Step2Form(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget, label="Date de l'événement")
    wilaya = forms.ChoiceField(choices=WILAYA_CHOICES, label="Wilaya")

class Step3Form(forms.Form):
    lieu = forms.ChoiceField(choices=VENUE_CHOICES, label="Type de lieu")

class Step4Form(forms.Form):
    services = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Services supplémentaires",
        required=False
    )

