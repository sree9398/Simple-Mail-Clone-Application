from django.contrib import admin
from .models import Login  # Import your Mail model

class MailAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # Replace with the actual field names from your Mail model

# Register your model with the admin site
admin.site.register(Login, MailAdmin)
