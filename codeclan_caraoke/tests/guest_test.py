import unittest
# import guest.py file
from classes.guest import *
from classes.room import *
from classes.song import *
from classes.drink import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Gavin Will", 100.00, "Rock and Roll")
        self.poor_guest = Guest("Oscar", 2.00, "No fave song")
        self.room = Room("Room One", 10.00) 
        self.song1 = Song("The Velvet Underground", "Rock and Roll", 1)
        self.song2 = Song("The Zombies", "She's Not There", 2)
        self.song3 = Song("The Mamas and Papas", "California Dreamin'", 3)
        self.drink1 = Drink("Tennents", 3.00)
        self.drink2 = Drink("Guinness", 3.50)
        self.drink3 = Drink("Red Wine", 4.00)

    def test_guest_pays_for_room(self):
        self.guest.paying_for_room(self.room)
        self.assertEqual(90, self.guest.wallet)
        
    def test_guest_has_name(self):
        self.assertEqual("Gavin Will", self.guest.name)

    def test_guess_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)



    def test_guests_favourite_song_is_on_playlist(self):
        self.room.add_song_to_list(self.song1)
        self.room.add_song_to_list(self.song2)
        self.room.add_song_to_list(self.song3)
        self.assertEqual("Oh wow my favourite song!", self.guest.favourite_song_on_the_list(self.room.room_song_list, self.guest))

    def test_sufficient_drink_funds__true_if_enough(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.drink1))
    
    def test_sufficient_drink_funds__false_if_not_enough(self):
        self.assertEqual(False, self.poor_guest.sufficient_funds(self.drink3))
    
    def test_customer_can_buy_drink__decreases_money(self): 
        self.guest.buy_drink(self.drink1)
        self.assertEqual(97.00, self.guest.wallet)


