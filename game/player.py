

class Player:

    #Building the constructor of the class with its attributes
    def __init__(self):

        self.score = 300
        self.bet = None
    
    #Guess if the next card will be higher or lower
    def guess(self):

        guess = input("Higher or lower? [h/l] ")
        self.bet = guess