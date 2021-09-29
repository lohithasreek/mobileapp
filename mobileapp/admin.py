from django.contrib import admin
from .models import Mobile
# Register your models here.
class Mobileadmin(admin.ModelAdmin):
    readonly_fields=['Ordered_Date']

admin.site.register(Mobile,Mobileadmin)

