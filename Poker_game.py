
#%%
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