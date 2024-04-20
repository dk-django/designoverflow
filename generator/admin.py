from django.contrib import admin

from .models import DalleGeneration

@admin.register(DalleGeneration)
class DalleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'user_prompt', 'dalle_response', 'created_at']
    list_editable = ['user_prompt']
    list_filter = ['owner', 'user_prompt', 'created_at']
    search_fields = ['user_prompt__istartswith', 'dalle_response__istartswith']
