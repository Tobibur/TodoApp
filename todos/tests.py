from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from .models import Category
from .serializers import CategorySerializer
from django.urls import reverse
from rest_framework.views import status


# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_category(name=""):
        if name != "":
            Category.objects.create(name=name)

    def setUp(self):
        self.create_category("Studying")
        self.create_category("Chores")
        self.create_category("Shopping")


class GetAllCategories(BaseViewTest):

    def test_get_all_categories(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("categories-all")
        )
        # fetch the data from db
        expected = Category.objects.all()
        serialized = CategorySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
