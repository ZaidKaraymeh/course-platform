from django.test import TestCase

# Create your tests here.

from .models import *
from .utils.helpers import subtract_new_average, add_new_average
from decimal import Decimal 

class RatingTests(TestCase):
    
    def test_add_new_average(self):
        avg = 4.7
        count = 3
        value = 3
        expected_avg = Decimal('4.3')
        new_average = add_new_average(avg, count, value)
        self.assertEqual(expected_avg, new_average)
        self.assertIsInstance(new_average, Decimal)

    def test_subtract_new_average(self):
        avg = 4.3
        count = 4
        value = 3
        expected_avg = Decimal('4.7')
        new_average = subtract_new_average(avg, count, value)
        self.assertEqual(expected_avg, new_average)
        self.assertIsInstance(new_average, Decimal)
