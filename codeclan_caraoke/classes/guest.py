class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

# removing room price from customers wallet        
    def paying_for_room(self, room):
        self.wallet -= room.hire_fee


    