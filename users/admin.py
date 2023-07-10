from django.contrib import admin

from users.models import User


# from products.admin import BasketAdmin


# Регистрация моделей для добавления данных через админ панель сайта
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

    # товары в корзине привязывается к пользователю
    # inlines = BasketAdmin
