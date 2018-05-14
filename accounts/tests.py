from django.test import TestCase
from accounts.models import Order


class OrderModelTests(TestCase):
    def test_is_empty(self):
        saved_orders = Order.objects.all()
        self.assertEqual(saved_orders.count(), 8)

