import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.services.models import Service, ServiceCategory

# القاموس المقترح سابقًا
service_categories = {
    "Coordination et planification": [
        "Coordination du programme",
        "Assistant personnel",
        "Wedding planner / Organisateur",
        "Organisation et planification"
    ],
    "Tenues et beauté": [
        "Tenues traditionnelles",
        "Maquillage",
        "Coiffure",
        "Location de robes",
        "Mode et beauté"
    ],
    "Cadeaux et souvenirs": [
        "Cadeaux personnalisés",
        "Boîtes souvenirs",
        "Cadeaux pour invités",
        "Cadeaux et souvenirs"
    ],
    "Transport": [
        "Motos",
        "Minibus / Bus",
        "Voiture de mariée",
        "Location de voitures de luxe",
        "Transport"
    ],
    "Décoration": [
        "Décoration traditionnelle",
        "Fleurs naturelles",
        "Éclairage",
        "Décoration de tables",
        "Décoration"
    ],
    "Divertissement": [
        "Groupes musicaux",
        "Musique live",
        "Animateur",
        "Divertissement"
    ],
    "Restauration": [
        "Boissons",
        "Pâtisseries",
        "Chefs privés",
        "Traiteur",
        "Cuisine"
    ],
    "Photographie et vidéo": [
        "Location de caméras",
        "Drone",
        "Vidéo",
        "Photographie"
    ],
    "Lieux de réception": [
        "Plage / Plein air",
        "Restaurant",
        "Petite salle privée",
        "Jardin",
        "Domicile",
        "Hôtel",
        "Salle des fêtes",
        "Lieux de réception"
    ]
}

for category_name, services in service_categories.items():
    category, created = ServiceCategory.objects.get_or_create(
        name_fr=category_name,
        defaults={'name_ar': category_name}  # يمكن تعديل الترجمة هنا لاحقًا
    )
    for service_name in services:
        Service.objects.get_or_create(
        name_fr=service_name,
        defaults={
        'name_ar': service_name,
        'category': category,
        'price': 0.00,  # ✅ سعر افتراضي
        'prestataire_id': 1,  # ⚠️ مطلوب إذا كانت العلاقة إلزامية
    }
)

print("✅ Insertion terminée avec succès.")
