# blackjack.py
# This program is for my final project and will be a close depiction to the
# card game blackjack


import random

def mainGame():
    # variables
    cards = ["King", "Queen", "Jack", "Ace", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    playerCards = []
    playerTotal = 0
    dealerCards = []
    dealerTotal = 0
    money = 0

    # function for pulling a random card
    def pullCard():
        x = random.choices(cards, k = 1)
        return x
    
    playGame = input("Welcome To Python Blackjack, Would you like to play (yes or no) >> ").lower()
    if playGame[0] == "y":
        if playerCards == []:
            for i in range(2):
                playerCards += pullCard()
                dealerCards += pullCard()
                
            # if statements for calculating total for both player and dealer
            for i in playerCards:
                if i == "King":
                    playerTotal += 10
                elif i == "Queen":
                    playerTotal += 10
                elif i == "Jack":
                    playerTotal += 10
                elif i == "Ace":
                    playerTotal += 11
                else:
                    playerTotal += i
            for i in dealerCards:
                if i == "King":
                    dealerTotal += 10
                elif i == "Queen":
                    dealerTotal += 10
                elif i == "Jack":
                    dealerTotal += 10
                elif i == "Ace":
                    dealerTotal += 11
                else:
                    dealerTotal += i

    elif playGame[0] == "n":
        exit()

    print(f"Player's Cards: {playerCards} Total: {playerTotal} {"\n"}Dealer's Cards: {dealerCards} Total: {dealerTotal}")
    




if __name__ == "__main__":
    mainGame()    