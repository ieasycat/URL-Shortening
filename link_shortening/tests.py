from django.test import TestCase
from link_shortening.views import reduction
from link_shortening.models import Link

# Create your tests here.


class RandomTest(TestCase):
    @staticmethod
    def test_reduction():
        url = reduction()
        assert len(url) == 28


class HomeTest(TestCase):
    def setUp(self):
        self.url = Link(
            url='https://www.onliner.by/',
            abbreviated_url='http://127.0.0.1:8000/oUgolG')

    def test_home(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    # Я так и не понял, как проверить вью с редиректорм
    # Объясни, если можно
    def test(self):
        result = self.client.get(self.url.url)
        self.assertEqual(result.status_code, 200)
