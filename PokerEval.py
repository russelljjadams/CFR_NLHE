# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:54:27 2016

@author: 4bet20x

"2c": 1,
"2d": 2,
"2h": 3,
"2s": 4,
"3c": 5,
"3d": 6,
...
"kh": 47,
"ks": 48,
"ac": 49,
"ad": 50,
"ah": 51,
"as": 52
"""

import array
import numpy as np
import random
from Deck import deck, r_deck 

handsDB = open('HandRanks.dat','rb')
ranks = array.array('i')
ranks.fromfile(handsDB, 32487834)


def LookupHand(hand):
    p = 53
    for card in hand:
        p = ranks[p + card]
    return p
    
def GetHandCategory(Hand):
    return Hand >> 12
    
def GetRank(Hand):
    return (Hand & 0x00000FFF)

def EquityVsRandom(hand,iterations=1000):   
    deck = list(range(1,53))
    deck.remove(hand[0])
    deck.remove(hand[1])
    
    win = 0
    for i in range(iterations):
        _deck = list(deck)
        
        villain = []
        villain.append(random.choice(_deck))
        _deck.remove(villain[0])
        villain.append(random.choice(_deck))
        _deck.remove(villain[1])
        
        board = random.sample(_deck,5)
        
        win += showdown(hand,villain,board)
            
    return (win / float(iterations))
            

def showdown(hero,vill,board):
    herohand = LookupHand(hero + board)
    villhand = LookupHand(vill + board)
    heroCat = GetHandCategory(herohand)
    villCat = GetHandCategory(villhand)
    if heroCat != villCat: return heroCat > villCat
    return GetRank(herohand) > GetRank(villhand)
    
def to_string(hero,vill,board):
    shero, svill, sboard = [], [], []
    for c in hero: shero.append(r_deck[c])
    for c in vill: svill.append(r_deck[c])
    for c in board: sboard.append(r_deck[c])
    return shero, svill, sboard
        
    
if __name__ == "__main__":   
    hero = [deck['Ac'],deck['As']]
    print(EquityVsRandom(hero, 500))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
