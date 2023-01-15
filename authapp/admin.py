from django.contrib import admin
from authapp.apps import AuthappConfig
from authapp.models import PortalUser

app_name = AuthappConfig.name

# Register your models here.

@admin.register(PortalUser)
class PortalUserModelAdmin(admin.ModelAdmin):
        list_display = ('username', 'first_name', 'last_name', 'created', 'updated')

