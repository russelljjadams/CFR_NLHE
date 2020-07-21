# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 01:05:54 2017

@author: 4bet20x
"""

from itertools import permutations

cards = '23456789TJQKA'
suits = 'csdh'
pairs = ['cs','cd','ch','sd','sh','dh']

UTG_Open = ['33+', 'ATs+', 'KTs+', 'QTs+', 'J9s+', 'T9s', '98s', '87s', '76s'
            , '65s', 'AJo+', 'KQo']
Snowie_UTG = ['55+', 'A2s+', 'K9s+', 'QTs+', 'JTs', 'T9s', 'ATo+', 'KJo+']


class RangeBuilder:
    def __init__(self,_range):
        self.range = _range
        self.new_range = []
        
    def parse_range(self):
        for hand in self.range:
            #Pairs
            if hand[0] == hand[1] and "+" in hand:
                self.pair_combos(hand[0])
            #Suited Combos i.e ATs+
            elif "s+" in hand:
                self.suited_combos(hand[0:2])
            #Single Combos i.e 65s
            elif "s" in hand:
                self.suited_single(hand[:-1])
            elif "o+" in hand:
                self.unsuited_combos(hand[0:2])
            elif "o" in hand:
                self.unsuited_single(hand[:-1])
            elif hand[0] == hand[1]:
                self.pair_single(hand[0])
            else:
                print "Error, hand uncategorized.", hand, hand
                
    def suited_single(self,hand):
        for suit in suits:
            self.new_range.append([hand[0]+suit,hand[1]+suit])
                
    def suited_combos(self, start):
        index = cards.index(start[1])
        while index != cards.index(start[0]):
            for suit in suits:
                self.new_range.append([start[0]+suit, cards[index]+suit])
            index+=1
            
    def unsuited_single(self,hand):
        for suit in permutations(suits,2):
            self.new_range.append([hand[0]+suit[0],hand[1]+suit[1]])
            
    def unsuited_combos(self, start):
        index = cards.index(start[1])
        while index != cards.index(start[0]):
            for suit in permutations(suits,2):
                self.new_range.append([start[0]+suit[0], cards[index]+suit[1]])
            index+=1
                
    def pair_single(self, pair):
        for suit in pairs:
            self.new_range.append([pair+suit[0],pair+suit[1]])
            
    def pair_combos(self, pair):
        index = cards.index(pair[0])
        while index != len(cards):
            for suit in pairs:
                self.new_range.append([cards[index]+suit[0],cards[index]+suit[1]])
            index+=1
                
        
if __name__ == "__main__":
    test = ['55']
    x = RangeBuilder(test)
    x.parse_range()
    print x.new_range, len(x.new_range)