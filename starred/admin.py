from django.contrib import admin
from starred.models import Starred

class mailAdmin(admin.ModelAdmin):
    list_display=('subject','recipient','message')

admin.site.register(Starred,mailAdmin)

# Register your models here.
