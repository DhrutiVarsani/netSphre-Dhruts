from django.contrib import admin
from alumni.models import Alumni, EduDetail, ProfessionalDetail, Connection, ConnectionRequest

# Register your models here.
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('alumni_id','name','dob','blood_group','gender','last_login','is_deleted','is_active')

class EduDetailAdmin(admin.ModelAdmin):
    list_display = ('edu_id','user','course','specialization','institute','entry_date','passout_date')

class ProfessionalDetailAdmin(admin.ModelAdmin):
    list_display = ('prof_id','alunmi','orgname','ocupation','start_date','end_date')

class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('conn_id','follower','following','since')

class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('conn_req_id','sender','receiver')


admin.site.register(Alumni,AlumniAdmin)
admin.site.register(EduDetail,EduDetailAdmin)
admin.site.register(ProfessionalDetail,ProfessionalDetailAdmin)
admin.site.register(Connection,ConnectionAdmin)
admin.site.register(ConnectionRequest,ConnectionRequestAdmin)
