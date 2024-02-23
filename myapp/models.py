from django.db import models
from accounts.models import User

# Create your models here.
class ToDos(models.Model):  
    title = models.CharField(max_length=150,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.content