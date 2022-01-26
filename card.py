import random

class Card:

    def __init__(self):
        
        self.card = [random.randint(0, 12)]
        self.displaying_card

    def displaying_card(self):
        self.card = [random.randint(0, 12)]
        return (self.card)


