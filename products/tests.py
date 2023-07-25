from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


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

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse("products:paginator", kwargs={"category_id": 0})
        response = self.client.get(path)

        self._common_products_tests(response)

        self.assertEqual(
            list(response.context_data["object_list"]), list(self.products[:3])
        )

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse("products:paginator", kwargs={"category_id": category.id})
        response = self.client.get(path)

        self._common_products_tests(response)

        self.assertEqual(
            list(response.context_data["object_list"]),
            list(self.products.filter(category_id=category.id)),
        )

    def _common_products_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Каталог")
        self.assertTemplateUsed(response, "products/products.html")
