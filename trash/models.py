from django.db import models

class Trash(models.Model):
    subject = models.CharField(max_length=255)
    recipient = models.EmailField()
    sent_date = models.DateTimeField(null=True)
    # Add any other fields you need to store in the Trash model

    def __str__(self):
        return self.subject
