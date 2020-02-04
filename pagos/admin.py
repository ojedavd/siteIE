from django.contrib import admin

from .models import Pagos

class PagosAdmin(admin.ModelAdmin):
    readonly_fields = ('user_created', 'user_modified', 'created', 'modified')

admin.site.register(Pagos, PagosAdmin)