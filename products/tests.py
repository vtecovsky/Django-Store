from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse("index")
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["title"], "Store")
        self.assertTemplateUsed(response, "products/index.html")


class ProductListViewTestCase(TestCase):
    # Initially, the test database will be filled with the objects from fixtures
    fixtures = ["categories.json", "products.json"]

    def test_list(self):
        path = reverse("products:paginator", kwargs={"category_id": 0})
        response = self.client.get(path)

        products = Product.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Каталог")
        self.assertTemplateUsed(response, "products/products.html")
        self.assertEqual(list(response.context_data["object_list"]), list(products[:3]))
