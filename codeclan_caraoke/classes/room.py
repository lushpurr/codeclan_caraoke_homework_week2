class Room:

    def __init__(self, name, hire_fee):
        self.name = name
        self.hire_fee = hire_fee
        self.room_capacity = 5
        self.room_song_list = []
        self.room_guest_list = []
        self.room_tab = []


# does customer have enough money to pay for room
    def can_customer_afford_room(self, guest, room):
        if guest.wallet >= room.hire_fee:
            return True
        else: 
            return False

# add customer to room list
    def add_to_booking(self, guest):
        self.room_guest_list.append(guest)


# take a booking - remove money from customer and add to list
    def take_a_booking(self, room, guest):
        # #take customers money from function in guest class
        guest.paying_for_room(room)
        # #add customer to room list from function in self
        self.add_to_booking(guest)
   
# check out customer - clear room list
    def check_out_of_room(self, busy_room):
        return busy_room.clear()
    
# add song to room

    def add_song_to_list(self, song):
        self.room_song_list.append(song)

# has room reached capacity

    def has_room_reached_capacity(self, room_guest_list):
        if len(self.room_guest_list) <= self.room_capacity:
            return False
        else:
            return True

# tab calculation functions

    def tab_value(self):
        total = 0

        for drink in self.room_tab:
            total += drink.price

        return total

    def add_to_tab(self, drink):
        self.room_tab.append(drink)
        