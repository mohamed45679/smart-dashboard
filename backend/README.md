# Smart Dashboard Backend

لوحة تحكم ذكية مع Django REST API

## المتطلبات

- Python 3.10+
- MySQL (اختياري، يمكن استخدام SQLite للتطوير)

## التثبيت

```bash
cd backend
pip install -r requirements.txt
```

## إعداد قاعدة البيانات

### للتطوير (SQLite - افتراضي)
لا يتطلب أي إعداد إضافي.

### للإنتاج (MySQL)
1. قم بإنشاء قاعدة بيانات MySQL:
```sql
CREATE DATABASE smart_dashboard CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. عدّل `config/settings.py` وأزل التعليق عن إعدادات MySQL

## تشغيل السيرفر

```bash
# تطبيق التحديثات على قاعدة البيانات
python manage.py migrate

# إنشاء بيانات تجريبية
curl -X POST http://localhost:8000/api/seed/

# تشغيل السيرفر
python manage.py runserver
```

## API Endpoints

### المصادقة
- `POST /api/auth/register/` - تسجيل جديد
- `POST /api/auth/login/` - تسجيل دخول
- `POST /api/auth/logout/` - تسجيل خروج
- `GET /api/auth/me/` - المستخدم الحالي

### المهام
- `GET /api/tasks/` - جلب المهام
- `POST /api/tasks/` - إنشاء مهمة
- `PUT /api/tasks/{id}/` - تحديث مهمة
- `DELETE /api/tasks/{id}/` - حذف مهمة
- `PATCH /api/tasks/{id}/toggle/` - تبديل الإكمال

### الإشعارات
- `GET /api/notifications/` - جلب الإشعارات
- `PATCH /api/notifications/{id}/mark_read/` - تحديد كمقروء

### النشاطات
- `GET /api/activities/` - جلب النشاطات

### الإحصائيات
- `GET /api/statistics/dashboard/` - إحصائيات لوحة التحكم
- `GET /api/statistics/chart/` - بيانات الرسم البياني

## بيانات الدخول الافتراضية

```
البريد: admin@example.com
كلمة المرور: admin123
```
