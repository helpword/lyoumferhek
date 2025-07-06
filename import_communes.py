# import_communes.py
import os
import django
import json

# قم بإعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from your_app_name.models import Commune # استبدل your_app_name و Commune باسم تطبيقك ونموذجك

def import_data():
    file_path = 'communes.json' # تأكد من المسار الصحيح للملف

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            # افترض أن نموذجك لديه حقل 'name' وحقل 'wilaya'
            Commune.objects.create(name=item['name'], wilaya=item['wilaya'])
            print(f"تم إضافة البلدية: {item['name']}")

    except FileNotFoundError:
        print(f"الملف {file_path} غير موجود.")
    except Exception as e:
        print(f"حدث خطأ أثناء الاستيراد: {e}")

if __name__ == '__main__':
    import_data()