from django.contrib import admin

from dynamics.models import Site, Price, Note

# Register your models here.
admin.site.register(Site)
admin.site.register(Price)
admin.site.register(Note)
