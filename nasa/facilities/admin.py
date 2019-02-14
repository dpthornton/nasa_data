from django.contrib import admin
from .models import Facility


class FacilityAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Facility, FacilityAdmin)
