import os

EXPECTED_PROJECT_FOLDER = "lyoumferhek"
EXPECTED_APP = "services"
TEMPLATES_PATH = os.path.join(EXPECTED_APP, "templates", EXPECTED_APP, "home.html")

REQUIRED_FILES = [
    "manage.py",
    os.path.join(EXPECTED_PROJECT_FOLDER, "settings.py"),
    os.path.join(EXPECTED_PROJECT_FOLDER, "urls.py"),
    os.path.join(EXPECTED_PROJECT_FOLDER, "wsgi.py"),
    os.path.join(EXPECTED_PROJECT_FOLDER, "__init__.py"),
]

REQUIRED_APP_FILES = [
    os.path.join(EXPECTED_APP, "models.py"),
    os.path.join(EXPECTED_APP, "views.py"),
    os.path.join(EXPECTED_APP, "admin.py"),
    os.path.join(EXPECTED_APP, "urls.py"),  # يجب أن تُنشئه يدويًا
    TEMPLATES_PATH
]

def check_paths(paths, section_name):
    print(f"\n📁 التحقق من: {section_name}\n" + "-"*40)
    for path in paths:
        if os.path.exists(path):
            print(f"✅ موجود: {path}")
        else:
            print(f"❌ مفقود: {path}")

def check_manage_settings_reference():
    try:
        with open("manage.py", "r", encoding="utf-8") as f:
            content = f.read()
            if f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{EXPECTED_PROJECT_FOLDER}.settings')" in content:
                print("\n✅ ملف manage.py يشير إلى settings.py بشكل صحيح")
            else:
                print("\n❌ ⚠️ manage.py لا يشير إلى settings.py بشكل صحيح")
    except FileNotFoundError:
        print("\n❌ ملف manage.py غير موجود!")

def check_folders():
    print("\n📂 التحقق من المجلدات:")
    if os.path.isdir(EXPECTED_PROJECT_FOLDER):
        print(f"✅ مجلد المشروع '{EXPECTED_PROJECT_FOLDER}' موجود")
    else:
        print(f"❌ مفقود: مجلد المشروع '{EXPECTED_PROJECT_FOLDER}'")

    if os.path.isdir(EXPECTED_APP):
        print(f"✅ مجلد التطبيق '{EXPECTED_APP}' موجود")
    else:
        print(f"❌ مفقود: مجلد التطبيق '{EXPECTED_APP}'")

if __name__ == "__main__":
    print("🔍 التحقق من بنية مشروع Django 'LyoumFerhek'...\n")
    check_paths(REQUIRED_FILES, "ملفات المشروع الأساسية")
    check_paths(REQUIRED_APP_FILES, f"ملفات التطبيق '{EXPECTED_APP}'")
    check_manage_settings_reference()
    check_folders()
