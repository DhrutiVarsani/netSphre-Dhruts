from django.contrib import admin
from user.models import User

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('userid','email','password','userType')

admin.site.register(User,userAdmin)