from django.contrib import admin
from gadgets.models import Gadget, Brand

# Register your models here.
admin.site.register(Brand)
admin.site.register(Gadget)