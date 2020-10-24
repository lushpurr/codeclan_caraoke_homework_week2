import unittest

from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("The Velvet Underground", "Rock and Roll", 1)
        self.song2 = Song("The Zombies", "She's Not There", 2)
        self.song3 = Song("The Mamas and Papas", "California Dreamin'", 3)

    def test_song_has_artist(self):
        self.assertEqual("The Velvet Underground", self.song1.song_artist)

    def test_song_has_title(self):
        self.assertEqual("She's Not There", self.song2.song_title)

    def test_song_has_id(self):
        self.assertEqual(3, self.song3.song_id)