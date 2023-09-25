from django.db import models

class SentEmail(models.Model):
    subject = models.CharField(max_length=255)
    recipient = models.EmailField()
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
