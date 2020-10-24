import unittest
# import room.py here
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Dave", 200)
        self.guest1 = Guest("Julia", 100)
        self.guest2 = Guest("Caroline", 250)
        self.guest3 = Guest("Bill", 100)
        self.guest4 = Guest("Gavin", 60)
        self.guest5 = Guest("Ringo", 300)
        self.poor_guest = Guest("Oscar", 5)
        self.room = Room("One", 10)
        self.busy_room = [(self.guest, self.poor_guest)]
        self.song1 = Song("The Velvet Underground", "Rock and Roll", 1)
        self.song2 = Song("The Zombies", "She's Not There", 2)
        self.song3 = Song("The Mamas and Papas", "California Dreamin'", 3)


    def test_if_customer_has_enough_cash__True(self):
        self.assertEqual(True, self.room.can_customer_afford_room(self.guest, self.room))

    def test_if_customer_has_enough_cash__False(self):
        self.assertEqual(False, self.room.can_customer_afford_room(self.poor_guest, self.room))

    def test_add_a_booking(self):
        self.room.add_to_booking(self.guest)
        self.assertEqual(1, len(self.room.room_guest_list))

    def test_take_a_booking(self):
        self.room.take_a_booking(self.room, self.guest, )
        self.assertEqual(190, self.guest.wallet)
        self.assertEqual(1, len(self.room.room_guest_list))

    def test_check_out_of_room(self):
        self.room.check_out_of_room(self.busy_room)
        self.assertEqual(0, len(self.busy_room))

    def test_can_add_song_to_list__1(self):
        self.room.add_song_to_list(self.song1)
        self.assertEqual(1, len(self.room.room_song_list))

    def test_can_add_songs_to_list__3(self):
        self.room.add_song_to_list(self.song1)
        self.room.add_song_to_list(self.song2)
        self.room.add_song_to_list(self.song3)
        self.assertEqual(3, len(self.room.room_song_list))

    def test_room_has_reached_capacity__False(self):
        self.room.add_to_booking(self.guest)
        self.assertEqual(False, self.room.has_room_reached_capacity(self.room.room_guest_list))

    def test_room_has_reached_capacity__True(self):
        self.room.add_to_booking(self.guest)
        self.room.add_to_booking(self.guest1)
        self.room.add_to_booking(self.guest2)
        self.room.add_to_booking(self.guest3)
        self.room.add_to_booking(self.guest4)
        self.room.add_to_booking(self.guest5)
        self.assertEqual(True, self.room.has_room_reached_capacity(self.room.room_guest_list))


