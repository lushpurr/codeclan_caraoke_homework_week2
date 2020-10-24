class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

# removing room price from customers wallet        
    def paying_for_room(self, room):
        self.wallet -= room.hire_fee

    def favourite_song_on_the_list(self, song_list, guest):
        for song in song_list:
            if song.song_title == self.favourite_song:
                return "Oh wow my favourite song!"


    