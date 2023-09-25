from django.contrib import admin
from .models import Mail

class mailAdmin(admin.ModelAdmin):
    list_display=('from_mail','to_mail','subject','message')

admin.site.register(Mail,mailAdmin)

# Register your models here.
