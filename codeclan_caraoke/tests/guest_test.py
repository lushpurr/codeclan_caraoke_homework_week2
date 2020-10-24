import unittest
# import guest.py file
from classes.guest import *
from classes.room import *
from classes.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Gavin Will", 100, "Rock and Roll")
        self.room = Room("Room One", 10) 
        self.song1 = Song("The Velvet Underground", "Rock and Roll", 1)
        self.song2 = Song("The Zombies", "She's Not There", 2)
        self.song3 = Song("The Mamas and Papas", "California Dreamin'", 3)
 

    def test_guest_has_name(self):
        self.assertEqual("Gavin Will", self.guest.name)

    def test_guess_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)

    def test_guest_pays_for_room(self):
        self.guest.paying_for_room(self.room)
        self.assertEqual(90, self.guest.wallet)

    def test_guests_favourite_song_is_on_playlist(self):
        self.room.add_song_to_list(self.song1)
        self.room.add_song_to_list(self.song2)
        self.room.add_song_to_list(self.song3)
        self.assertEqual("Oh wow my favourite song!", self.guest.favourite_song_on_the_list(self.room.room_song_list, self.guest))





