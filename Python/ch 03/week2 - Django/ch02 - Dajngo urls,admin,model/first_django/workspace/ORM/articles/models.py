from django.db import models

# Create your models here.
class Article(models.Model):  # class 이름이 tablename으로 자동으로 됨
    title = models.TextField()  # models.CharField()로 해도 됨
    content = models.TextField()
    
    