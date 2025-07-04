import os
import sys
import django

# ✅ أضف المسار الجذر للمشروع إلى sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lyoumferhek.settings')
django.setup()

# ✅ استيراد الموديل
from services.models import EventLocationType

# ✅ قائمة أنواع المواقع
location_types = [
    "Salle des fêtes",
    "Jardin",
    "Ferme",
    "Espace ouvert",
    "Demeure privée",
    "Hôtel",
    "Terrasse",
    "Salle polyvalente",
    "Plage",
    "Restaurant",
    "Salle de conférence",
    "Château",
    "Rooftop",
    "Salle de spectacle",
    "Salle de réception",
    "Centre culturel",
    "Salle de banquet",
]

# ✅ إنشاء الأنواع في قاعدة البيانات
for name in location_types:
    obj, created = EventLocationType.objects.get_or_create(name=name)
    print(f"{'Créé' if created else 'Existe déjà'}: {obj.name}")
