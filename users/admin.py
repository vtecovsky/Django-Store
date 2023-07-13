from django.contrib import admin

from users.models import EmailVerification, User


# Регистрация моделей для добавления данных через админ панель сайта
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("code", "user", "expiration")
    fields = ("code", "user", "expiration", "created")
    readonly_fields = ("created",)
