from django.contrib import admin
from .models import *


@admin.register(Chanel)
class Chanel_admin(admin.ModelAdmin):
    #model = User
    list_display = ('id', 'name', 'start_time', 'end_time', 'type', 'active', 'language',)
    list_display_links = ('id', 'name',)
    list_editable = ('start_time', 'end_time', 'active', 'language', )
    pass


@admin.register(OriginPost)
class OriginPost_admin(admin.ModelAdmin):
    list_display = ('id', 'images', 'text', 'post_id',)
    list_display_links = ('id', 'text',)
    pass


@admin.register(ChanelPost)
class ChanelPost_admin(admin.ModelAdmin):
    list_display = ('id', 'chanel', 'self_post_id', 'origin_post',)
    list_display_links = ('id', 'chanel',)
    pass