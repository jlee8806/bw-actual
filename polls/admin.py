from django.contrib import admin

# Register your models here.
from .models import rsvp

class rsvpAdmin(admin.ModelAdmin):
    list_display = ['name', 'guest', 'email', 'attend', 'message']
    class Meta:
        model = rsvp


admin.site.register(rsvp, rsvpAdmin)
