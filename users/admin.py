from django.contrib import admin

from users.models import User

"Регистрация моделей для добавления данных через админ панель сайта"
admin.site.register(User)
