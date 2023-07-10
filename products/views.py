from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import ProductCategory, Product, Basket


# функции = контроллеры = вьюхи


def index(request):
    context = {}
    return render(request, "products/index.html", context)


def products(request, category_id=0, page_number=1):
    # Если категория приходит, то достаем только вещи из этой категории
    products = (
        Product.objects.filter(category_id=category_id)
        if category_id
        else Product.objects.all()
    )

    per_page = 3
    paginator = Paginator(products, per_page)

    # те же самые products, только с расширенными методами для работы с пагинаторами
    products_paginator = paginator.page(page_number)
    context = {
        "title": "Store - Каталог",
        "categories": ProductCategory.objects.all(),
        "products": products_paginator,
        "selected_category": category_id,
    }
    return render(request, "products/products.html", context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
