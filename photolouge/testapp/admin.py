# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Images

class ImageAdmin(admin.ModelAdmin):
    list_display = ('imageId','imageType')


admin.site.register(Images,ImageAdmin)
