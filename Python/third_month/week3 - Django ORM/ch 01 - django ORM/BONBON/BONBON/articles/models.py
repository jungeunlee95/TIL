from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"<{self.title} : {self.content}>"
    
    def __str__(self):
        return f"<{self.title} : {self.content}>"