from django.contrib import admin
from school.models import School,SchoolRec,Achievement
# Register your models here.

class schoolAdmin(admin.ModelAdmin):
    list_display = ('sid','orgid','name','address','is_deleted')

class SchoolRecAdmin(admin.ModelAdmin):
    list_display = ('recid','user','school','entry_date','exit_date','entry_class','passout_class')

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('achieve_id','alumni','achieve_date','achieve_desc','cetrificate','is_deleted')


admin.site.register(School,schoolAdmin)
admin.site.register(SchoolRec,SchoolRecAdmin)
admin.site.register(Achievement,AchievementAdmin)