# blackjack.py
# This program is for my final project and will be a close depiction to the
# card game blackjack


import random

def mainGame():
    cards = ["King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    playerCards = []
    dealerCards = []
    money = 0

    def pullCard():
        x = random.choices(cards, k = 1)
        return x
    
    playGame = input("Welcome To Python Blackjack, Would you like to play (yes or no) >> ").lower()
    if playGame[0] == "y":
        if playerCards == []:
            playerCards += pullCard()
            dealerCards += pullCard()
    elif playGame[0] == "n":
        exit()

    




if __name__ == "__main__":
    mainGame()    