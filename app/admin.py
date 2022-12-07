from django.contrib import admin
from .models import events,invites,invited
# Register your models here.
admin.site.register(events)
admin.site.register(invites)
admin.site.register(invited)