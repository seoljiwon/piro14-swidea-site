from django.contrib import admin
from .models import Ideas, DevTool


@admin.register(Ideas)
class CustomIdeasAdmin(admin.ModelAdmin):
    pass


@admin.register(DevTool)
class CustomDevToolAdmin(admin.ModelAdmin):
    pass
