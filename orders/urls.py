from django.urls import path

from orders.views import OrderCreateView
from products.views import ProductsListView, basket_add, basket_remove

app_name = "orders"

urlpatterns = [
    path("order_create/", OrderCreateView.as_view(), name="order_create"),
]
