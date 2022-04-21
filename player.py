# Classe Player pour BlackJack
#
# Date : 21/04/2022
# Auteur : Matthieu LEVASSEUR


class Player():
    name = str
    hand = [str]
    value = int
    splitted = bool
    owner = str
    bet = int

    def __init__(self,name)->None:
        self.name=name
        self.splitted = False
        self.owner = ""

    def __init__(self,name,owner)->None:
        self.name=name
        self.splitted = True
        self.owner = owner

    def hit(self,sabot):
        self.hand.append(sabot.getCard())
        self.value = sabot.getHandValue(self.hand)

    #def split(self,sabot,card):
    #    split = Player("split",self.name)
    #    split.bet = self.bet
    #    split.append(card)
    #    split.value = sabot.getHandValue(split.value)
    #    self.hand.remove(self.hand[1])
    #    return split

    def newBet(self,bet):
        self.bet += bet

    def double(self):
        self.bet += self.bet

    def reset(self):
        self.hand.clear()
        self.splitted = False

    def display(self):
        txt = ""
        for i in range(len(self.hand)):
            txt+=self.hand[i]
            if i < len(self.hand)-1:
                txt+=" "
        txt+="\nValue :"+str(self.value)

        

