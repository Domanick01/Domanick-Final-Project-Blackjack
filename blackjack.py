# blackjack.py
# This program is for my final project and will be a close depiction to the
# card game blackjack


import random

def mainGame():
    # variables
    cards = ["King", "Queen", "Jack", "Ace", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    playerCards = []
    amount = 0
    playerTotal = 0
    dealerCards = []
    dealerTotal = 0
    money = 0

    # function for pulling a random card
    def pullCard():
        x = random.choices(cards, k = 1)
        return x
    
    # function for defining face value cards
    def faceValues(x):
        if x == "King":
            return 10
        elif x == "Queen":
            return 10
        elif x == "Jack":
            return 10
        elif x == "Ace":
            return 11
        else:
            return x
    
    playGame = input("Welcome To Python Blackjack, Would you like to play (yes or no) >> ").lower()
    if playGame[0] == "y":
        if playerCards == []:
            for i in range(2):
                playerCards += pullCard()
                amount += 1
                dealerCards += pullCard()
                
            # if statements for calculating total for both player and dealer
            for i in playerCards:
                playerTotal += faceValues(i)
            for i in dealerCards:
                dealerTotal += faceValues(i)

        print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
        
        while playerTotal and dealerTotal <= 21:
            nextMove = input("What is your next move (hit, stand, double) >> ").lower
            if nextMove == "hit":
                print("NEXT MOVE HAS RAN")
                playerCards += pullCard()
                playerTotal += faceValues(playerCards[amount])
                print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")

    elif playGame[0] == "n":
        exit()
    else:
        mainGame()

    print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
    




if __name__ == "__main__":
    mainGame()    