import random

#class Card:
#
#    def __init__(self):
#        
#        self.card = [random.randint(0, 12)]
#        self.displaying_card
#
#    def displaying(self):
#        self.card = [random.randint(0, 12)]
#        return (self.card)

class Card:
    
    def __init__(self):

        self.card_number = 0

    
    def shuffle(self):

        number = random.randint(1, 13)
        self.card_number = number

    def display(self):

        return self.card_number
