from django.urls import path

from products.views import products, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path("baskets/add/<int:product_id>/", basket_add, name="basket_add"),
    path(
        "category/<int:category_id>/page/<int:page_number>/", products, name="catinator"
    ),  # name=category+paginator
    path("baskets/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
]
