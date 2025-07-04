# services/load_prestataires.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lyoumferhek.settings')
django.setup()

from services.models import Prestataire, ServiceCategory, Service

prestataires_data = [
    {
        "name": "Studio Lumière",
        "phone": "0550 123 456",
        "category": "Photographie",
        "service_name": "Photographe",
        "price": 25000
    },
    {
        "name": "Chef Ahmed",
        "phone": "0560 987 321",
        "category": "Cuisine",
        "service_name": "Chef Cuisine",
        "price": 40000
    },
    {
        "name": "DJ Sam",
        "phone": "0770 333 111",
        "category": "Musique",
        "service_name": "DJ",
        "price": 30000
    },
    {
        "name": "Groupe El Ferah",
        "phone": "0778 111 222",
        "category": "Animation",
        "service_name": "Groupe musical",
        "price": 35000
    },
    {
        "name": "Zorna Boualem",
        "phone": "0666 777 888",
        "category": "Animation",
        "service_name": "Zerna",
        "price": 20000
    },
    {
        "name": "Art Déco",
        "phone": "0555 888 999",
        "category": "Décoration",
        "service_name": "Décoration",
        "price": 30000
    },
]

for p in prestataires_data:
    cat, _ = ServiceCategory.objects.get_or_create(name=p['category'])
    prest, _ = Prestataire.objects.get_or_create(name=p['name'], phone=p['phone'])
    Service.objects.get_or_create(
        name=p['service_name'],
        category=cat,
        prestataire=prest,
        price=p['price']
    )

print("✅ Prestataires et services ajoutés avec succès.")
