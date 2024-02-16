from django.contrib import admin
from message.models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id','message','send','receive','time','is_deleted')

admin.site.register(Message, MessageAdmin)