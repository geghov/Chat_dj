from django.contrib import admin
from .models import Message
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'created']
    list_display_links = ['id', 'text']
