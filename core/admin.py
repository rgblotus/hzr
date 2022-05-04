from django.contrib import admin

from .models import Indent, IndentInstance, Indentor,  Order, Vendor

# Register your models here.

admin.site.register(Indentor)
admin.site.register(Indent)
admin.site.register(IndentInstance)
admin.site.register(Vendor)
admin.site.register(Order)
