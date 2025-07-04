import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lyoumferhek.settings")
django.setup()

from services.models import Wilaya, Commune

# تحميل البيانات
with open("services/Wilaya_Of_Algeria.json", encoding="utf-8") as f:
    wilayas_data = json.load(f)

with open("services/Commune_Of_Algeria.json", encoding="utf-8") as f:
    communes_data = json.load(f)

# حذف السابق
Wilaya.objects.all().delete()
Commune.objects.all().delete()

# استيراد الولايات
for w in wilayas_data:
    Wilaya.objects.create(code=int(w["id"]), name=w["name"])

print(f"[✅] {len(wilayas_data)} wilayas imported.")

# استيراد البلديات
communes_created = 0
for c in communes_data:
    try:
        wilaya = Wilaya.objects.get(code=int(c["wilaya_id"]))
        Commune.objects.create(name=c["name"], wilaya=wilaya)
        communes_created += 1
    except Wilaya.DoesNotExist:
        print(f"[⚠️] Wilaya not found for: {c}")

print(f"[✅] {communes_created} communes imported.")
