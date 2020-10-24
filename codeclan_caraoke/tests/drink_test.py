import unittest

from classes.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Tennents", 3.00)
        self.drink2 = Drink("Guinness", 3.50)
        self.drink3 = Drink("Red Wine", 4.00)


    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.00, self.drink3.price)