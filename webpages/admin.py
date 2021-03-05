from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def my_photo(self, object):
        img_url = object.photo.url
        return format_html('<img src="{}" width="40" height="40" />'.format(img_url))

    list_display = ('id', 'my_photo', 'first_name', 'role', 'created_date', )
    list_display_links = ('first_name', 'id', 'my_photo', )
    search_fields = ('first_name', 'role', )
    list_filter = ('role', )


# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
