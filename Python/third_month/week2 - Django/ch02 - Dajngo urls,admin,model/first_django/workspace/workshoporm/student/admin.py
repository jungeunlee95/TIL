from django.contrib import admin
from .models import Student   # 현재폴더의 models.py의 Student
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birthday', 'age',)
    
admin.site.register(Student)