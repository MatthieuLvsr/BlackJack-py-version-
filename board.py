# Classe Board pour BlackJack
#
# Date : 21/04/2022
# Auteur : Matthieu LEVASSEUR

from player import Player,Bank
from sabot import Sabot

class Board():
    bank = Bank
    players = []
    sabot = Sabot

    def __init__(self,decks,nbPlayers)->None:
        self.bank = Bank()
        for i in range(nbPlayers):
            name = input("Nom du joueur "+str(i+1)+" : ")
            self.players.append(Player(name,50))
        self.sabot = Sabot(decks)

    def newRound(self):
        self.bank.reset()
        self.bank.hit(self.sabot)
        for i in range(len(self.players)):
            self.players[i].reset()
            self.players[i].hit(self.sabot)
            self.players[i].hit(self.sabot)
            self.players[i].getTurn(self.sabot,self.bank)
        self.bank.end(self.sabot)

# DEBUG ZONE

test = Board(6,5)
test.newRound()