from django.contrib import admin

# Register your models here.
from main.models import *


@admin.register(Products)
class Products(admin.ModelAdmin):
    list_display = ['sku','name','dollar_amount','category','size']

    def dollar_amount(self, obj):
        return "$%s" % obj.price if obj.price else ""
