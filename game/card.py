import random

class Card:
    
    def __init__(self):

        self.__card_number = None

    
    def shuffle(self):

        number = random.randint(1, 14)
        self.__card_number = number

    def display(self):

        return self.__card_number
