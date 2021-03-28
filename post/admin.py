from django.contrib import admin
from post.models import *
# Register your models here.

class SearchResultStoreAdmin(admin.ModelAdmin):
    list_display = ('search_key_store', 'date_time_fields',)
    list_filter = ["date_time_fields"]
admin.site.register(SearchResultStore, SearchResultStoreAdmin)

admin.site.register(Category)
admin.site.register(Post)

