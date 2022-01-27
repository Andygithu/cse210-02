from game.card import Card
from game.player import Player


class Director:

    def __init__(self):

        self.card = Card()
        self.card_number = 0
        self.bet = ""
        self.next_card = Card()
        self.next_card_number = 0
        self.score = Player().score
        #self.round_score = 0
        #self.total_score = 0
        self.is_playing = True

    def start_game(self):

        while self.is_playing:
            self.get_bet()
            self.display_next_card()
            self.display_result() 


    def get_bet(self):

 #Test change
        """
        Displays card's current number and aks
        for the player's bet for the next card
        """
        
        self.card.shuffle()
        self.card_number = self.card.display()
        print(f"\nThe card is: {self.card_number}")

        player_bet = Player()
        self.bet = player_bet.guess()

    def display_next_card(self):

        """
        Display next card's number and define it this
        number was higher or lower than player's bet
        """
        self.next_card.shuffle()
        self.next_card_number = self.next_card.display()


        higher = None
        lower = None
        equal = None

        if self.next_card_number > self.card_number:
            higher = True
        elif self.next_card_number < self.card_number:
            lower = True
        elif self.next_card_number == self.card_number:
            equal = True

        if self.bet == "h" and higher == True:
            #self.round_score = 100
            self.score += 100
        elif self.bet == "l" and lower == True:
            self.score += 100
            #self.round_score = 100
        elif self.bet == "h" and lower == True:
            self.score -= 75
            #self.round_score = -75
        elif self.bet == "l" and higher == True:
            self.score -= 75
            #self.round_score = -75
        elif equal:
            print("No points added or lost. Cards were the same.")
        else:
            print("Invalid input. No points added or lost.")
        
        if self.score <= 0:
            print("You've ran our of points.")
            print("Game over.")
            self.is_playing = False

        if self.is_playing:
            print(f"Next card was: {self.next_card_number}")

        #self.total_score += self.round_score
        

    def display_result(self):

        if self.is_playing:

            print(f"Your score is: {self.score}")
            play_again = input("Play again? [y/n] ")
            play_again = play_again.lower() == "y"

            self.is_playing = play_again