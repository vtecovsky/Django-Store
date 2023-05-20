from django.shortcuts import render

# функции = контроллеры = вьюхи


def index(request):
    context = {
        'title': "Test Title",
        'is_promotion': False,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
    }
    return render(request, 'products/products.html')