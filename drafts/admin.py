from django.contrib import admin
from drafts.models import Drafts

class mailAdmin(admin.ModelAdmin):
    list_display=('subject','recipient','message')

admin.site.register(Drafts,mailAdmin)

# Register your models here.
