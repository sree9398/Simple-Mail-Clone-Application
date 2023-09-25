from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.

class Mail(models.Model):
    #model for mail sending 
    from_mail = models.CharField('from', max_length=100)
    to_mail   = models.EmailField('to',max_length=100)
    subject   = models.TextField()
    message  = models.TextField()


    