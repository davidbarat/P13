from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# from search.models import Product, Category
# from .tests_models import ModelTest
    
    
def test_index_page(self):
    response = self.client.get(reverse("index"))
    self.assertEqual(response.status_code, 200)