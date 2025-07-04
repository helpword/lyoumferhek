from django import forms
from .models import Prestataire, Client
from services.models import Wilaya, Commune

EVENT_CHOICES = [
    ('mariage', 'Mariage'),
    ('fiancailles', 'Fiançailles'),
    ('anniversaire', 'Anniversaire'),
    ('nouveau_ne', 'Nouveau-né'),
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
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.order_by('code'), label="Wilaya")
    commune = forms.ModelChoiceField(queryset=Commune.objects.none(), label="Commune")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wilaya'].label_from_instance = lambda obj: f"{obj.code} - {obj.name}"
        self.fields['commune'].label_from_instance = lambda obj: f"{obj.name}, {obj.wilaya.name}"

class WilayaCommuneForm(forms.Form):
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.order_by('code'), label="Wilaya")
    commune = forms.ModelChoiceField(queryset=Commune.objects.none(), label="Commune")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wilaya'].label_from_instance = lambda obj: f"{obj.code} - {obj.name}"
        self.fields['commune'].label_from_instance = lambda obj: f"{obj.name}, {obj.wilaya.name}"

class Step3Form(forms.Form):
    lieu = forms.ChoiceField(choices=VENUE_CHOICES, label="Type de lieu")

class Step4Form(forms.Form):
    services = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Services supplémentaires",
        required=False
    )
