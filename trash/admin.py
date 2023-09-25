from django.contrib import admin
from trash.models import Trash

class mailAdmin(admin.ModelAdmin):
    list_display=('subject','recipient','sent_date')

admin.site.register(Trash,mailAdmin)

# Register your models here.
