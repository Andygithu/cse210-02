from game.card import Card
from game.player import Player


class Director:

    def __init__(self):

        self.card = Card()
        self.bet = None
        self.next_card = Card()
        self.score = 0
        self.total_score = 0
        self.is_playing = True

    def start_game(self):

        while self.is_playing:
            get_bet()
            display_next_card()
            display_result()


    def get_bet(self):

        """
        Displays card's current number and aks
        for the player's bet for the next card
        """
            
        card = self.card.shuffle()
        print(f"The card is: {card}")
        self.card = card

        player_bet = Player.guess()
        self.bet = player_bet

    def display_next_card(self):

        """
        Display next card's number and define it this
        number was higher or lower than player's bet
        """

        next_card = self.next_card.shuffle()
        print(f"Next card was: {next_card}")

        higher = next_card > self.card
        lower = next_card < self.card

        if self.bet == "h" and higher:
            self.score = 100
        elif self.bet == "l" and lower:
            self.score = 100
        elif self.bet == "h" and lower:
            self.score -= 75
        elif self.bet == "l" and higher:
            self.score -= 75
        
        if self.score <= 0:
            print("You've ran our of points.")
            print("Game over.")
            self.is_playing = False

        self.total_score += self.score
        
    
    def display_result(self):