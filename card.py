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

        self.__card_number = None

    
    def shuffle(self):

        number = random.randint(1, 14)
        self.__card_number = number

    def display(self):

        return self.__card_number


