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
    def _init_(self,number,suite):       
        self.number=number
        number=[2,3,4,5,6,7,8,9,10,J,Q,K,A]
        self.suite=suite
        suite=['clubs','spades','hearts','diamonds']
        
class Card_hand:
    def _init_(self,cards):
        self.cards=cards
        
        hand=random.sample(card,5)
 
#%%
card1 = Card()#this is object
card2 = Card()








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
