from django.contrib import admin
from . models import File, Client

# Register your models here.

class FilesInline(admin.TabularInline):  # new
    model = File
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','veh_reg']
    search_fields = ['name','veh_reg']
    inlines =[FilesInline, ]
admin.site.register(File)
admin.site.register(Client,ClientAdmin)



admin.site.site_header = "FMS Admin Panel"
admin.site.site_title = "FMS"
admin.site.index_title = "Welcome to FMS Admin"