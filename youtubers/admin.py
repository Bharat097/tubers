from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html


class YtAdmin(admin.ModelAdmin):

    def my_photo(self, object):
        img_url = object.photo.url
        return format_html('<img src="{}" width="40" height="40" />'.format(img_url))

    list_display = ('id', 'my_photo', 'name', 'subs_count', 'is_featured',)
    search_fields = ('name', 'camera',)
    list_filter = ('city', 'camera_type',)
    list_display_links = ('id', 'name',)
    list_editable = ('is_featured',)


# Register your models here.
admin.site.register(Youtuber, YtAdmin)
