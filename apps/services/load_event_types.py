import os
import sys
import django

# أضف المسار إلى جذر المشروع حيث مجلد lyoumferhek
sys.path.append(r'E:\LyoumFerhek')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from services.models import EventType

event_types = [
    "Mariage",
    "Fiançailles",
    "Anniversaire",
    "Nouveau-né",
    "Baptême",
    "Réception",
]

for et in event_types:
    obj, created = EventType.objects.get_or_create(name=et)
    if created:
        print(f"Created event type: {et}")
    else:
        print(f"Event type already exists: {et}")
