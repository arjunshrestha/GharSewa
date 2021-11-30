from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Status)
admin.site.register((Contact, Service, BookService, BookUpdate))


@admin.register(Customer, Service_Man)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
