from django.contrib import admin
from menus.models import MenuItem
from menus.forms import MenuItemForm


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)
