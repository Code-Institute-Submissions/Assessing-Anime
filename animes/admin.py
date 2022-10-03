from django.contrib import admin
from .models import Item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):
    list_display = ('item_name', 'slug', 'status', 'created_on')
    search_fileds = ['item_name', 'item_content']
    prepopulated_fields = {'slug': ('item_name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('item_content')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)



