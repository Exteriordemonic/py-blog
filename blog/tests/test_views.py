from django.test import TestCase
from django.urls import reverse


class IndexTestCase(TestCase):
    def setUp(self):
        self.url = reverse("blog:index")

    def test_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
