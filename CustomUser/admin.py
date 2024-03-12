from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("username",)
    ordering = ("username",)

    def has_module_perms(self, request, obj=None):
        return True


# Enregistrez votre modèle avec l'administration Django en utilisant la classe d'administration personnalisée
admin.site.register(CustomUser, CustomUserAdmin)
