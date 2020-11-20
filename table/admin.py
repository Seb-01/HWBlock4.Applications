from django.contrib import admin
from table.models import Table, CsvPath
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Table,TableAdmin)

class CsvPathAdmin(admin.ModelAdmin):
    pass

admin.site.register(CsvPath,CsvPathAdmin)