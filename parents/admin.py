from django.contrib import admin
from .models import Parent

# Register your models here.
class ParentAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'last_name', 'birthday', 'posted_at']
  search_fields = ('name',)


admin.site.register(Parent, ParentAdmin)
