# blackjack.py
# This program is for my final project and will be a close depiction to the
# card game blackjack


import random

def mainGame():
    # player variables
    playerCards = []
    playerAmount = 0
    playerTotal = 0
    money = 0
    # dealer variables
    dealerCards = []
    dealerAmount = 0
    dealerTotal = 0
    # game variables
    cards = ["King", "Queen", "Jack", "Ace", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    winner = ""

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
                playerAmount += 1
                dealerCards += pullCard()
                dealerAmount += 1

            # if statements for calculating total for both player and dealer
            for i in playerCards:
                playerTotal += faceValues(i)
            for i in dealerCards:
                dealerTotal += faceValues(i)

        print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
        
        while playerTotal and dealerTotal <= 21:
            nextMove = input("What is your next move (hit, stand, double) >> ").lower()
            newPlayerCards = playerCards
            newDealerCards = dealerCards
            if nextMove == "hit":
                newPlayerCards += pullCard()
                playerAmount += 1
                playerTotal += faceValues(playerCards[len(playerCards)])
                print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
            elif nextMove == "stand":
                while dealerTotal <= 16:
                    newDealerCards += pullCard()
                    dealerAmount += 1
                    print(len(dealerCards) - 1)
                    dealerTotal += faceValues(dealerCards[(len(dealerCards) - 1)])
                    break
                print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
    
    
    
    
    elif playGame[0] == "n":
        exit()
    else:
        mainGame()

    print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
    




if __name__ == "__main__":
    mainGame()    