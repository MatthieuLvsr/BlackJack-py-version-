# Classe Board pour BlackJack
#
# Date : 21/04/2022
# Auteur : Matthieu LEVASSEUR

from os import system
from player import Player,Bank
from sabot import Sabot

class Board():
    bank = Bank
    players = []
    sabot = Sabot

    def __init__(self,decks,nbPlayers)->None:
        system("cls")
        self.bank = Bank()
        for i in range(nbPlayers):
            name = input("Nom du joueur "+str(i+1)+" : ")
            self.players.append(Player(name,50))
        self.sabot = Sabot(decks)

    def newRound(self):
        system("cls")
        self.bank.reset()
        self.bank.hit(self.sabot)
        for i in range(len(self.players)):
            self.players[i].reset()
            self.players[i].getBet()
        for j in range(len(self.players)):
            self.players[j].hit(self.sabot)
            self.players[j].hit(self.sabot)
            self.players[j].getTurn(self.sabot,self.bank)
        self.bank.end(self.sabot)
        self.checkWin()

    def checkWin(self):
        txt = ""
        for i in range(len(self.players)):
            if self.players[i].value>self.bank.value and self.players[i].value<=21:
                self.players[i].win()
            elif self.players[i].value==self.bank.value:
                self.players[i].draw()
            if self.players[i].splitted==True:
                if self.players[i].splitHand.value>self.bank.value and self.players[i].splitHand.value<=21:
                    self.players[i].win()
                elif self.players[i].value==self.bank.value:
                    self.players[i].draw()
            txt+=self.players[i].name + " : " + str(self.players[i].money) + "$\n"
        print(txt)
        input()
        
            
            

# DEBUG ZONE

test = Board(6,2)
test.newRound()
