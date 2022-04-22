# Classe Player pour BlackJack
#
# Date : 21/04/2022
# Auteur : Matthieu LEVASSEUR


from os import system


class Player():
    name = str
    hand = []
    value = int
    splitted = bool
    splitHand = None
    bet = int
    money = int

    def __init__(self,name,money=None)->None:
        self.name=name
        self.splitted = False
        self.bet = 0
        self.money = money

    def hit(self,sabot,card=None):
        self.hand.append(sabot.getCard(card))
        self.value = sabot.getHandValue(self.hand)

    def split(self,sabot):
        if self.hand[0]==self.hand[1] and len(self.hand)==2 and self.money >= self.bet:
            self.splitted = True
            self.hand.remove(self.hand[1])
            split = Split(self,self.hand[0])
            split.hit(sabot)
            self.hit(sabot)
            self.splitHand = split

    def newBet(self,bet):
        if self.money >= bet:
            self.bet += bet
            self.money -= bet
            return True
        else:return False

    def double(self,sabot):
        if self.newBet(self.bet):
            self.hit(sabot)

    def reset(self):
        self.hand.clear()
        if self.splitted:
            self.splitHand.reset()
        self.splitted = False
        self.bet = 0
        self.splitHand = None

    def getTurn(self,sabot,bank):
        choice = None
        while choice != "s" and self.value<=21:
            system("cls")
            print(bank.toString())
            print(self.toString())
            if self.splitted == True:print("First hand")
            if self.money>=self.bet and self.splitted==False and self.hand[0]==self.hand[1]:
                choice = input("\nStay(s) - Hit(h) - Double(d) - Split(p) : ")
            elif self.money>=self.bet and len(self.hand)==2:
                choice = input("\nStay(s) - Hit(h) - Double(d) : ")
            else:choice = input("\nStay(s) - Hit(h) : ")
            if choice == "p":self.split(sabot)
            elif choice == "d":
                self.double(sabot)
                choice = "s"
            elif choice == "h":self.hit(sabot)
        if self.splitted == True:self.splitHand.getTurn(sabot,bank)
        system("cls")
        print(bank.toString())
        print(self.toString())

    def toString(self)->str:
        txt=self.name
        txt+= "\nCards : "
        for i in range(len(self.hand)):
            txt+=self.hand[i]
            if i < len(self.hand)-1:
                txt+=" "
        if self.splitted == True:
            txt+="   "
            for i in range(len(self.splitHand.hand)):
                txt+=self.splitHand.hand[i]
                if i < len(self.splitHand.hand):
                    txt+=" "
        txt+="\nValue : "+str(self.value)
        if self.splitted == True:
            for i in range(len(self.hand)-1):
                txt+="  "
            if self.value<10:txt+=" "
            txt+="  "+str(self.splitHand.value)
        txt+="\n"
        return txt

class Split():
    owner = Player
    hand = []
    value = int
    splitted = bool
    bet = 0
    def __init__(self,owner,card) -> None:
        self.owner = owner
        self.splitted = True
        self.newBet(self.owner.bet)
        self.hand.append(card)

    def newBet(self,bet):
        if self.owner.money >= bet:
            self.bet += bet
            self.owner.money -= bet
            return True
        else:return False

    def hit(self,sabot,card=None):
        self.hand.append(sabot.getCard(card))
        self.value = sabot.getHandValue(self.hand)

    def double(self,sabot):
        if self.newBet(self.bet):
            self.hit(sabot)

    def getTurn(self,sabot,bank):
        choice = None
        while choice != "s" and self.value<=21:
            system("cls")
            print(bank.toString())
            print(self.owner.toString())
            print("Second hand")
            if self.owner.money>=self.bet and self.splitted==False and self.hand[0]==self.hand[1]:
                choice = input("\nStay(s) - Hit(h) - Double(d) - Split(p) : ")
            elif self.owner.money>=self.bet and len(self.hand)==2:
                choice = input("\nStay(s) - Hit(h) - Double(d) : ")
            else:choice = input("\nStay(s) - Hit(h) : ")
            if choice == "p":self.split(sabot)
            elif choice == "d":
                self.double(sabot)
                choice = "s"
            elif choice == "h":self.hit(sabot)

    def reset(self):
        self.hand.clear()
        self.bet = 0
        self.value = 0

class Bank():
    min = int
    hand = []
    value = int

    def __init__(self,min=16) -> None:
        self.min = min

    def hit(self,sabot,card=None):
        self.hand.append(sabot.getCard(card))
        self.value = sabot.getHandValue(self.hand)

    def reset(self):
        self.hand.clear()
        self.value = 0

    def toString(self):
        txt = "BANK"
        txt+= "\nCards : "
        for i in range(len(self.hand)):
            txt+=self.hand[i]
            if i < len(self.hand)-1:
                txt+=" "
        txt+="\nValue : "+str(self.value)+"\n"
        return txt
            


# DEBUG ZONE

# from sabot import Sabot

# sabot_test = Sabot(6)
# test = Player("test",20)
# bank = Bank()
# bank.hit(sabot_test)
# test.newBet(6)
# test.hit(sabot_test,"8")
# test.hit(sabot_test,"8")
# test.getTurn(sabot_test,bank)
# print(newSplit.toString())

        

