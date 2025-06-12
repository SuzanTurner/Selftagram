from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = "Images")
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.user.username} - {self.image.name}"
    
    
    
