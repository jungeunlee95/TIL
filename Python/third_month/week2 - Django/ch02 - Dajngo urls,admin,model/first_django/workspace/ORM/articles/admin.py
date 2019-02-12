from django.contrib import admin
from .models import Article    # 현재폴더의 models.py의 Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    
admin.site.register(Article, ArticleAdmin)