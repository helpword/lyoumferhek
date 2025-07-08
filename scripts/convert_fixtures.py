import json
import os

# المسارات إلى ملفاتك الأصلية
base_path = "fixtures"
wilaya_path = os.path.join(base_path, "wilayas.json")
commune_path = os.path.join(base_path, "communes.json")

# تحميل بيانات الولايات
with open(wilaya_path, encoding="utf-8") as f:
    wilayas = json.load(f)

# تحميل بيانات البلديات
with open(commune_path, encoding="utf-8") as f:
    communes = json.load(f)

# تجهيز fixture الولايات
wilayas_fixture = []
for i, w in enumerate(wilayas, start=1):
    wilayas_fixture.append({
        "model": "wilayas.wilaya",  # عدّلها حسب اسم الـ app
        "pk": i,
        "fields": {
            "code": w.get("code") or w.get("id"),
            "name": w.get("name"),
            "name_ar": w.get("name_ar") or w.get("name_arabe"),
        }
    })

# حفظ fixture الولايات
with open(os.path.join(base_path, "wilayas_fixture.json"), "w", encoding="utf-8") as f:
    json.dump(wilayas_fixture, f, ensure_ascii=False, indent=2)

# تجهيز fixture البلديات
communes_fixture = []
for i, c in enumerate(communes, start=1):
    communes_fixture.append({
        "model": "wilayas.commune",  # عدّلها حسب اسم الـ app
        "pk": i,
        "fields": {
            "name": c.get("name"),
            "name_ar": c.get("name_ar") or c.get("name_arabe"),
            "zip_code": c.get("zip_code") or c.get("postal_code") or "",
            "wilaya": c.get("wilaya_code") or c.get("wilaya_id") or 1
        }
    })

# حفظ fixture البلديات
with open(os.path.join(base_path, "communes_fixture.json"), "w", encoding="utf-8") as f:
    json.dump(communes_fixture, f, ensure_ascii=False, indent=2)

print("✅ Fixtures جاهزة: wilayas_fixture.json و communes_fixture.json")
