from django.db import models

# Create your models here.
class Student(models.Model):  # class 이름이 tablename으로 자동으로 됨
    name = models.CharField(max_length=25)  
    email = models.CharField(max_length=25)  
    birthday = models.DateField()  
    age = models.IntegerField()     
    
    def __str__(self):
        return f"이름 : {self.name}, 나이 : {self.age}, 생일 : {self.birthday}, 이메일 : {self.email}"