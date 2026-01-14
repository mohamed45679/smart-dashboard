# API Models for Smart Dashboard
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """Extended User model with additional fields"""
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
    role = models.CharField(max_length=50, default='user')
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username


class Task(models.Model):
    """Task model for todo items"""
    PRIORITY_CHOICES = [
        ('low', 'منخفضة'),
        ('medium', 'متوسطة'),
        ('high', 'عالية'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tasks'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Notification(models.Model):
    """Notification model"""
    TYPE_CHOICES = [
        ('info', 'معلومات'),
        ('success', 'نجاح'),
        ('warning', 'تحذير'),
        ('error', 'خطأ'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='info')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'notifications'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Activity(models.Model):
    """Activity log model"""
    TYPE_CHOICES = [
        ('success', 'نجاح'),
        ('info', 'معلومات'),
        ('warning', 'تحذير'),
        ('danger', 'خطر'),
    ]
    
    ICON_CHOICES = [
        ('check', 'علامة صح'),
        ('user', 'مستخدم'),
        ('alert', 'تنبيه'),
        ('x', 'إغلاق'),
        ('message', 'رسالة'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='info')
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='info')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-created_at']
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return self.title
    
    @property
    def time_ago(self):
        """Return human-readable time difference"""
        now = timezone.now()
        diff = now - self.created_at
        
        if diff.days > 0:
            return f'منذ {diff.days} يوم'
        elif diff.seconds >= 3600:
            hours = diff.seconds // 3600
            return f'منذ {hours} ساعة'
        elif diff.seconds >= 60:
            minutes = diff.seconds // 60
            return f'منذ {minutes} دقيقة'
        else:
            return 'منذ لحظات'


class Statistics(models.Model):
    """Daily statistics model"""
    record_date = models.DateField(unique=True)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    active_users = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    products_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    services_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    subscriptions_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    consulting_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'statistics'
        ordering = ['-record_date']
        verbose_name_plural = 'Statistics'
    
    def __str__(self):
        return f'Statistics for {self.record_date}'
