from django.contrib import admin
from products.models import ProductCategory, Product, Basket

# Регистрация моделей для добавления данных через админ панель сайта
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')

    # Отвечает за отображение одного предмета в панели администратора
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')

    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


# TabularInline можно применять, когда есть связь ForeignKey
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('products', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
