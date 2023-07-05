from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory, Product, Basket


# функции = контроллеры = вьюхи


def index(request):
    context = {}
    return render(request, "products/index.html", context)


def products(request, category_id=None):
    # Если категория приходит, то достаем только вещи из этой категории
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)

    else:
        products = Product.objects.all()

    context = {
        "title": "Store - Каталог",
        "categories": ProductCategory.objects.all(),
        "products": products
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
