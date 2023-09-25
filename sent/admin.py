from django.contrib import admin
from sent.models import SentEmail

class mailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'message', 'sent_date')

admin.site.register(SentEmail, mailAdmin)
