[app]

# اسم التطبيق كما يظهر للمستخدم
title = الصندوق

# معرّف الحزمة (الاسم البرمجي) — أحرف إنجليزية وأرقام فقط
package.name = hesabat

# نطاق الحزمة — يكوّن المعرّف الكامل: org.omar.hesabat
package.domain = org.omar

# مجلد المصدر (الجذر الحالي)
source.dir = .

# الامتدادات التي تُضمّن داخل الـ APK (مهم: ttf للخط العربي)
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,db

# تضمين مجلد الخطوط بشكل صريح
source.include_patterns = assets/fonts/*

# إصدار التطبيق
version = 1.0

# الاعتماديات — لا تغيّر إصدار kivymd لتفادي مشاكل البناء
# python-bidi مثبّت على 0.4.2 (نقي بايثون) لأن الإصدارات الأحدث تعتمد على Rust ولا تُبنى
requirements = python3,kivy==2.3.0,kivymd==1.1.1,arabic_reshaper,python-bidi==0.4.2,sqlite3,openpyxl,et_xmlfile,plyer,pyjnius

# اتجاه الشاشة
orientation = portrait

# شاشة كاملة (0 = إظهار شريط الحالة)
fullscreen = 0

# أيقونة التطبيق (قاصة)
icon.filename = %(source.dir)s/assets/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# صلاحيات (التخزين اختياري؛ القاعدة تُحفظ داخل بيانات التطبيق)
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# مستويات الـ API
android.api = 33
android.minapi = 21
android.ndk = 25b

# المعماريات المدعومة
android.archs = arm64-v8a, armeabi-v7a

# السماح بالنسخ الاحتياطي
android.allow_backup = 1

# قبول تراخيص الـ SDK تلقائياً (مفيد للبناء الآلي)
android.accept_sdk_license = True
