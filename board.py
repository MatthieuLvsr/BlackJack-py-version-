# Classe Board pour BlackJack
#
# Date : 21/04/2022
# Auteur : Matthieu LEVASSEUR

from player import Player
from sabot import Sabot

class Board():
    bank = Player
    players = [Player]
    sabot = Sabot

    def __init__(self,decks,nbPlayers)->None:
        self.bank = Player("Banque")
        for i in range(nbPlayers):
            name = "Joueur"+str(i)
            self.players.append(Player(name))
        self.sabot = Sabot(decks)

    def newRound(self):
        self.bank.hit(self.sabot)
        for i in range(len(self.players)):
            self.players[i].hit(self.sabot)
            self.players[i].hit(self.sabot)