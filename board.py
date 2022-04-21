# Classe Board pour BlackJack
#
# Date : 21/04/2022
# Auteur : Matthieu LEVASSEUR

from player import Player
from sabot import Sabot

class Board():
    bank = Player
    player1 = Player
    sabot = Sabot
    def __init__(self,decks):
        self.bank = Player("Banque")
        self.player1 = Player("Joueur")
        self.sabot = Sabot(decks)