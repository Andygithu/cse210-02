import random

class Player:

    def guessing():
    
       choice = ""

       cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

       choice = input('Would you like to continue playing? (y/n) ')

       if choice == 'y':
           card = cards[random.randint(0, 12)]
           print(f'Current Card: {card}')
       elif choice == 'n':
            print('Thanks for playing. End of game.')
       elif choice != 'y' and choice != 'n':
             print('Error, your choice is not available')