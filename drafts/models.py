from django.db import models

class Drafts(models.Model):
    subject = models.CharField(max_length=255)
    recipient = models.EmailField()
    message=models.TextField()
    # Add any other fields you need to store in the Trash model

    def __str__(self):
        return self.subject
