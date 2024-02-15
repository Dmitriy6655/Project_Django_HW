from django.contrib import admin
from .models import Client, Goods, Order


# функция для изменения данных
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)


# Колонки отображаемые в админ. панеле Django
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount', 'create_at']  # список отображаемых продуктов
    ordering = ['price', '-amount']  # сортировка
    list_filter = ['price', 'create_at', 'amount']  # фильтрование
    search_fields = ['price']
    search_help_text = "Поиск по цене (price) "
    actions = [reset_quantity]

    """Отдельный продукт"""
    fields = ['name', 'price', 'amount', 'create_at']
    readonly_fields = ['create_at']


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'create_at')





class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'price', 'create_at']


admin.site.register(Client, ClientAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
