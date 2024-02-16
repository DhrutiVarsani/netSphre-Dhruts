from django.contrib import admin
from tenant.models import organisation

# Register your models here.
class orgAdmin(admin.ModelAdmin):
    list_display = ('orgid','name','address','is_deleted')


admin.site.register(organisation,orgAdmin)