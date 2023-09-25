from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True,unique=True)
    password = models.CharField(max_length=128,null=True)  # Storing the hashed password
    
    def __str__(self):
        return self.username
