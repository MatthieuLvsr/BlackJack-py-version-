# Classe Sabot pour BlackJack
# 
# date : 21/04/2022
# Auteur : Matthieu LEVASSEUR

import random


class Sabot():
    LIST_CARDS = [
        "2","3","4","5",
        "6","7","8","9",
        "10","J","Q","K","A",
    ]
    nbDeck = int
    cards = []

    def __init__(self,nb)->None:
        self.nbDeck = nb
        self.fill()
        

    def fill(self)->None:
        self.cards.clear()
        for i in range(self.nbDeck):
            for j in range(len(self.LIST_CARDS)):
                self.cards.append(self.LIST_CARDS[j])
        random.shuffle(self.cards)

    def getCard(self,card=None)->str:
        if card != None:
            if card not in self.cards:self.fill()
            newCard = card
            for i in range(len(self.cards)):
                if card == self.cards[i]:
                    self.cards.remove(self.cards[i])
                    break
        else:
            if self.isEmpty():self.fill()
            newCard = self.cards[0]
            self.cards.remove(self.cards[0])
        return newCard

    def isEmpty(self)->bool:
        if len(self.cards)==0:return True
        else: return False

    def getvalue(self,card)->int:
        if card == "2":return 2
        if card == "3":return 3
        if card == "4":return 4
        if card == "5":return 5
        if card == "6":return 6
        if card == "7":return 7
        if card == "8":return 8
        if card == "9":return 9
        if card == "10":return 10
        if card == "J":return 10
        if card == "Q":return 10
        if card == "K":return 10
        if card == "A":return 11

    def getHandValue(self,hand)->int:
        value = 0
        for i in range(len(hand)):
            value += self.getvalue(hand[i])
        if value > 21 and "A" in hand:value -= 10
        return value


# DEBUG ZONE

# test = Sabot(6)
# hand = []
# hand.append(test.getCard())
# hand.append(test.getCard())
# print(hand)
# print(test.getHandValue(hand))