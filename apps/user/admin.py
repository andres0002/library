from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.user.models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('username', 'email', 'name', 'lastname')
    list_display = ('username', 'email', 'name', 'lastname', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    source_class = UserResource

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(ContentType)
