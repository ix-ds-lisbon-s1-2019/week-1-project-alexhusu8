#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:29:27 2019

@author: alexandersu
"""
#%%
import sys
import random as rand
number_players=sys.argv[0]
print(number_players)

int(number_players)

for i in range(number_players):
	name=input("enter your name")
	print("your name is {}".format(name))
    
    
ls=[2,3,4,5,6,7,8,9,10,'j','q','k','a']*4
dicto={}
ps=[]
for player in range(int(number_players)):
    koko=rand.sample(ls,5)
    ps.append(koko)
    for i in koko:
        ls.remove(i)
    dicto[player]=koko

print(dicto)

for lists in ps:
    for ind in lists:
        if ind is 'j':
            lists[lists.index(ind)]=11
        elif ind is 'q':
            lists[lists.index(ind)]=12
        elif ind is 'k':
            lists[lists.index(ind)]=13
        elif ind is 'a':
            lists[lists.index(ind)]=14
        else:
            pass


for x in ps:
    x.sort(reverse=True)
    
highest_cards=[]

for x in ps:
    max(x)
    highest_cards.append(max(x))
    
print(highest_cards)

winning_card=[]
winning_card.append(max(highest_cards))

print(winning_card)

if len(winning_card)==1:
    print("The person with {} won the game!"(winning_card).format)
elif len(winning_card) > 1:
    print("There was a tie, nobody wins the game!")
    
    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:23:37 2019

@author: alexandersu
"""
import sys

number_players=sys.argv[1]
print(number_players)

for i in range(number_players):
	name=input("enter your name")
	print("your name is {}".format(name))
    
for i in range(number_players):
    hand=[]
    hand.append()

#%%
class Person:
    def _init_(self,card_hand):
        self.card_hand=card_hand
        
class Card:
    def __init__(self,number,suite):       
        self.number=number
        number=[2,3,4,5,6,7,8,9,10,J,Q,K,A]
        self.suite=suite
        suite=['clubs','spades','hearts','diamonds']
        
class Card_hand:
    def __init__(self,cards):
        self.cards=cards
        
        hand=random.sample(card,5)
 
#%%
class Cardd:
    def __init__(self, number, suite):       
        self.number=number
        self.suite=suite
        
    def __desco__(self):
        return self.suite 


card_1 = Cardd(2, 'hearts')

suite=['clubs','spades','hearts','diamonds']
number=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
x=[1,2,3,4,5]
for i in range(5):
    x=random.choice(number)
    y=random.choice(suite)
 #this is object
    card_i=Cardd(number=x, suite=y)


x1=card_1.__desco__()
x2=card_2.__desco__()
x3=card_3.__desco__()
x4=card_4.__desco__()
x5=card_5.__desco__()

card_hand=[x1,x2,x3,x4,x5]

card_hand
#%%
class Cardd:
    
    def __init__(self, number, suite):       
        self.number=number
        self.suite=suite
        
    def __desco__(self):
        ls=[]
        ls.append(self.number)
    def kok(self):
        return self.__desco__()

card_1 = Cardd(2, 'hearts')

suite=['clubs','spades','hearts','diamonds']
number=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
x=random.choice(number)
y=random.choice(suite)
card1=Cardd(number=x, suite=y)
card1.kok()

 #%%      
class hand_print:
    def printed_hand(self):
        print(card_hand)
        
hand_print





#%%
#attempt at code for winning hand

class winning_hand:
    def winning(self):
        
#%%
import random

class number_players:
    def number_of_plyers(self):
        self=input()
        print("There are {} players".format(self))
        
        


class card_hand:
    def number(self):        
        self.number=[2,3,4,5,6,7,8,9,10,J,Q,K,A]
    def suite(self):
        self.suite=['clubs','spades','hearts','diamonds']
        
class winning_hand:
    def winner(self):
        print("player {} won!".format(winner))
        

#%%
def number_of_players(x):
    isinstance(x,int)
    str(integer)
    if isinstance(x,int) == True:
        print('please enter integer')
    else:
        return x

print(number_of_players())
        
#%%
class card:
    def _init_(self,number,suite):       
        self.number=number
        number=[2,3,4,5,6,7,8,9,10,J,Q,K,A]
        self.suite=suite
        suite=['clubs','spades','hearts','diamonds']
        
class card_hand:
    def hand(self):
        hand=random.sample(card,5)
        
class hand_print:
    def printed_hand(self):
        print(card_hand)


card_hand.random.choice(number,suite,5)
#%%
def sort(card_hand):
    card_hand.sort()
#%%
#create a dictionary and assign a card to each player by saying "for x in number of players" then 
#sort the values and then compare the first element of each list
# just convert the dictionary into lists
#%%
if _gt_(cardhand) then :
    print('playerx wins')
sort the cards, then compare the first elements of each list
#%%
import sys

number_players=sys.argv[1]
print(number_players)

for i in range(number_players):
	name=input("enter your name")
	print("your name is {}".format(name))
    
import random
deck = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'jack':11, 'queen':12, 'king':13, 'Ace':14}

for i in range(number_player):
    hand=[]
    hand=random