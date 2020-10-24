import unittest
# import guest.py file
from classes.guest import *
from classes.room import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Gavin Will", 100)
        self.room = Room("Room One", 10)  

    def test_guest_has_name(self):
        self.assertEqual("Gavin Will", self.guest.name)

    def test_guess_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)

    def test_guest_pays_for_room(self):
        self.guest.paying_for_room(self.room)
        self.assertEqual(90, self.guest.wallet)





