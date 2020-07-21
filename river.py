# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 04:20:04 2017

@author: 4bet20x

Will Tipton - Expert Heads Up No Limit Hold'Em V1 - Page 48 - Equilibriation Exercise
"""
import random
from RangeBuilder import RangeBuilder
from Deck import deck, r_deck
from PokerEval import showdown

board = ['Js','6h','3s','Jd','2d']
hero_range = [['Ac','Jc'], ['Kc','Jc'],['Qc','Jc'],['Jc','Tc'],['5c','4c'],
    ['Kc','Jh'],['Qc','Jh'], ['Kd','Jc'],['Qd','Jc'],['5d','4d'],
    ['Kd','Jh'],['Qd','Jh'],['Kh','Jc'],['Qh','Jc'],['Ah','2h'],
    ['Ah','5h'],['Ah','8h'],['Ah','Jh'],['Kh','Jh'],['Qh','Jh'],['Jh','Th'],
    ['As','Tc'],['Ks','Jc'],['Qs','Jc'],['As','Td'],['As','Th'],['Ks','Jh'],
    ['Qs','Jh'],['Qs','6s'],['Qs','7s'],['Qs','8s'],['Qs','9s'],
    ['Qs','Ts'],['Ts','7s'],['9s','7s'],['8s','7s'],
    ['3d','3c'],['3h','3c'],['3h','3d'],['6s','6c'],['6d','6c'],['6d','6s'],['As','Ac'],
    ['Ad','Ac'],['Ah','Ac']]
hero_test = [['As','Td'], ['Ac','Jc']]
hero_test = [['Ah','2h']]

villain_range = [['Jc', 'Jh'], ['Tc', 'Ts'], ['Tc', 'Td'], ['Tc', 'Th'], 
            ['Ts', 'Td'], ['Ts', 'Th'], ['Td', 'Th'], ['9c', '9s'], 
            ['9c', '9d'], ['9c', '9h'], ['9s', '9d'], ['9s', '9h'], 
            ['9d', '9h'], ['8c', '8s'], ['8c', '8d'], ['8c', '8h'], 
            ['8s', '8d'], ['8s', '8h'], ['8d', '8h'], ['7c', '7s'], 
            ['7c', '7d'], ['7c', '7h'], ['7s', '7d'], ['7s', '7h'], 
            ['7d', '7h'], ['5c', '5s'], ['5c', '5d'], ['5c', '5h'], 
            ['5s', '5d'], ['5s', '5h'], ['5d', '5h'], ['4c', '4s'], 
            ['4c', '4d'], ['4c', '4h'], ['4s', '4d'], ['4s', '4h'], 
            ['4d', '4h'], ['Ac', '6c'], ['As', '6s'], ['Ad', '6d'], 
            ['Ac', '3c'], ['Ad', '3d'], ['Ah', '3h'], ['Kc', 'Jc'], 
            ['Kh', 'Jh'], ['Kc', '6c'], ['Ks', '6s'], ['Kd', '6d'], 
            ['Qc', 'Jc'], ['Qh', 'Jh'], ['Qc', '6c'], ['Qs', '6s'], 
            ['Qd', '6d'], ['Jc', '2c'], ['Jh', '2h'], ['Jc', '3c'], 
            ['Jh', '3h'], ['Jc', '4c'], ['Jh', '4h'], ['Jc', '5c'], 
            ['Jh', '5h'], ['Jc', '6c'], ['Jc', '7c'], ['Jh', '7h'], 
            ['Jc', '8c'], ['Jh', '8h'], ['Jc', '9c'], ['Jh', '9h'], 
            ['Jc', 'Tc'], ['Jh', 'Th'], ['6c', '4c'], ['6s', '4s'], 
            ['6d', '4d'], ['6c', '3c'], ['6d', '3d'], ['6c', '2c'], 
            ['6s', '2s'], ['Ac', '6s'], ['Ac', '6d'], ['As', '6c'], 
            ['As', '6d'], ['Ad', '6c'], ['Ad', '6s'], ['Ah', '6c'], 
            ['Ah', '6s'], ['Ah', '6d'], ['Kc', '6s'], ['Kc', '6d'], 
            ['Ks', '6c'], ['Ks', '6d'], ['Kd', '6c'], ['Kd', '6s'], 
            ['Kh', '6c'], ['Kh', '6s'], ['Kh', '6d'], ['Qc', '6s'], 
            ['Qc', '6d'], ['Qs', '6c'], ['Qs', '6d'], ['Qd', '6c'], 
            ['Qd', '6s'], ['Qh', '6c'], ['Qh', '6s'], ['Qh', '6d'], 
            ['Jc', '4s'], ['Jc', '4d'], ['Jc', '4h'], ['Jh', '4c'], 
            ['Jh', '4s'], ['Jh', '4d'], ['Jc', '5s'], ['Jc', '5d'], 
            ['Jc', '5h'], ['Jh', '5c'], ['Jh', '5s'], ['Jh', '5d'], 
            ['Jc', '6s'], ['Jc', '6d'], ['Jh', '6c'], ['Jh', '6s'], 
            ['Jh', '6d'], ['Jc', '7s'], ['Jc', '7d'], ['Jc', '7h'], 
            ['Jh', '7c'], ['Jh', '7s'], ['Jh', '7d'], ['Jc', '8s'], 
            ['Jc', '8d'], ['Jc', '8h'], ['Jh', '8c'], ['Jh', '8s'], 
            ['Jh', '8d'], ['Jc', '9s'], ['Jc', '9d'], ['Jc', '9h'], 
            ['Jh', '9c'], ['Jh', '9s'], ['Jh', '9d'], ['Jc', 'Ts'], 
            ['Jc', 'Td'], ['Jc', 'Th'], ['Jh', 'Tc'], ['Jh', 'Ts'], 
            ['Jh', 'Td'], ['Tc', '6s'], ['Tc', '6d'], ['Ts', '6c'], 
            ['Ts', '6d'], ['Td', '6c'], ['Td', '6s'], ['Th', '6c'], 
            ['Th', '6s'], ['Th', '6d'], ['9c', '6s'], ['9c', '6d'], 
            ['9s', '6c'], ['9s', '6d'], ['9d', '6c'], ['9d', '6s'], 
            ['9h', '6c'], ['9h', '6s'], ['9h', '6d'], ['8c', '6s'], 
            ['8c', '6d'], ['8s', '6c'], ['8s', '6d'], ['8d', '6c'], 
            ['8d', '6s'], ['8h', '6c'], ['8h', '6s'], ['8h', '6d'], 
            ['7c', '6s'], ['7c', '6d'], ['7s', '6c'], ['7s', '6d'], 
            ['7d', '6c'], ['7d', '6s'], ['7h', '6c'], ['7h', '6s'], 
            ['7h', '6d'], ['6c', '5s'], ['6c', '5d'], ['6c', '5h'], 
            ['6s', '5c'], ['6s', '5d'], ['6s', '5h'], ['6d', '5c'], 
            ['6d', '5s'], ['6d', '5h'], ['Ts', '4s'], ['Ts', '5s'], 
            ['Ts', '6s'], ['Ts', '7s'], ['Ts', '8s'], ['Ts', '9s'], 
            ['9s', '4s'], ['9s', '5s'], ['9s', '6s'], ['9s', '7s'], 
            ['9s', '8s'], ['8s', '4s'], ['8s', '5s'], ['8s', '6s'], 
            ['8s', '7s'], ['7s', '6s'], ['6s', '5s'], ['3d', '3c'], 
            ['6d', '6c'], ['Qs', 'Qc'], ['Qd', 'Qc'], ['Qh', 'Qc'], 
            ['Ks', 'Kc'], ['Kd', 'Kc'], ['Kh', 'Kc'], ['As', 'Ac'], 
            ['Ad', 'Ac'], ['Ah', 'Ac']]
            
vill_test = [['Jc', 'Jh'], ['Tc', 'Ts'],['As', '6s'],['Qs', '6s']]
vill_test = [['Ks','Kc'],['Kd','Kc'],['Kh','Kc'],['As','Ac']]
     

# Step 1: Get current mixed strategy through regret-matching.
# Step 2: Get random action according to mixed-strategy distribution.
# Step 3: Train
# Step 4: Get average mixed strategy across all training iterations.
        
class Poker_Player:
    def __init__(self,serial,strategy):
        self.serial = serial
        self.actions = 2
        self.strategy = self.create_strategy(strategy)
        
    def create_strategy(self, player_range):
        strategy = {}
        for hand in player_range:
            # Can't hash a list
            hand = tuple(hand)
            strategy[hand] = {
               "strategy":[0]*self.actions, "strategySum":[0]*self.actions, 
                 "regretSum":[0]*self.actions, "avgStrategy":[0]*self.actions}
        return strategy

    def getStrategy(self,hand):
        for a in range(self.actions):
            if self.strategy[hand]["regretSum"][a] > 0:
                self.strategy[hand]["strategy"][a] = self.strategy[hand]["regretSum"][a]
            else:
                self.strategy[hand]["strategy"][a] = 0
        normalizingSum = sum(self.strategy[hand]["strategy"])

        for a in range(self.actions):
            if normalizingSum > 0:
                self.strategy[hand]["strategy"][a] /= float(normalizingSum)
            else:
                self.strategy[hand]["strategy"][a] = 1.0 / self.actions
            self.strategy[hand]["strategySum"][a] += self.strategy[hand]["strategy"][a]

    def getAction(self,hand):
        r = random.random()
        a = 0
        cumulativeProbability = 0.0
        while a < (self.actions):
            cumulativeProbability += self.strategy[hand]["strategy"][a]
            if r < cumulativeProbability:
                return a
            a+=1
            
    def getAverageStrategy(self, iterations):
        for hand in self.strategy:
            normalizingSum = sum(self.strategy[hand]["strategy"])
            for a in range(2):
                if normalizingSum > 0:
                    self.strategy[hand]["avgStrategy"][a] = self.strategy[hand]["strategySum"][a] / normalizingSum / iterations
                else:
                    self.strategy[hand]["avgStrategy"][a] = 1.0 / 2



def river(hero_range, vill_range, board, iterations):
    pot, eff_stack = 53, 48.5
    p1, p2 = Poker_Player(1,hero_range), Poker_Player(2,vill_range)
    
    #Train
    for i in xrange(iterations):
        hand2 = tuple(random.choice(vill_range))
        unique = False
        while unique == False:
            hand = tuple(random.choice(hero_range))
            unique = True
            for c in hand:
                if c in hand2: 
                    unique = False
            

        # Get regret-matched mixed strategy actions
        p1.getStrategy(tuple(hand))
        p2.getStrategy(tuple(hand2))
        
        #Get Random action according to mixed-strategy distribution
        p1Action = p1.getAction(hand)
        p2Action = p2.getAction(hand2)
        
        sutility = showdown_utility(hand,hand2,board)
        
        if sutility:
            p1_utilities = [[eff_stack,eff_stack],[eff_stack*2+pot, eff_stack+pot]]
            p2_utilities = [[eff_stack+pot,eff_stack+pot],[0, eff_stack]]
        else:
            p1_utilities = [[eff_stack,eff_stack],[0,eff_stack+pot]]
            p2_utilities = [[eff_stack+pot,eff_stack+pot],[eff_stack*2+pot, eff_stack]]

     # Accumulate Action Regrets # Train 
        p1nodeUtil = 0
        p2nodeUtil = 0
        for a in range(2):
            p1nodeUtil += p1.strategy[hand]["strategy"][a] * p1_utilities[a][p2Action]
            p2nodeUtil += p2.strategy[hand2]["strategy"][a] * p2_utilities[p1Action][a]
        for a in range(2):
            p1.strategy[hand]["regretSum"][a] += (p1_utilities[a][p2Action] - p1nodeUtil)
            p2.strategy[hand2]["regretSum"][a] += (p2_utilities[p1Action][a] - p2nodeUtil)


    p1.getAverageStrategy(iterations)
    p2.getAverageStrategy(iterations)
    calls = 0
    callsavg = 0
    for hand in p1.strategy:
        #print hand, p1.strategy[hand]
        if p1.strategy[hand]["strategy"][0] < p1.strategy[hand]["strategy"][1]:
            calls += 1
        if p1.strategy[hand]["avgStrategy"][0] < p1.strategy[hand]["avgStrategy"][1]:
            callsavg += 1      
    print "Shoves: ", calls
    print "AvgShoves: ", callsavg
    
    calls = 0
    callsavg = 0
    for hand in p2.strategy:
        #print p2.strategy[hand]
        #print hand, p2.strategy[hand]['avgStrategy'], p2.strategy[hand]["strategy"]
        if p2.strategy[hand]["strategy"][0] > p2.strategy[hand]["strategy"][1]:
            calls += 1
        if p2.strategy[hand]["avgStrategy"][0] > p2.strategy[hand]["avgStrategy"][1]:
            callsavg += 1      
    print "Calls: ", calls
    print "AvgCalls: ", callsavg
#
#    for hand in p2.strategy:
#        print hand
#        print p2.strategy[hand]["avgStrategy"]
                    
def showdown_utility(v1,v2,board):
    _v1 = [deck[v1[0]],deck[v1[1]]]
    _v2 = [deck[v2[0]],deck[v2[1]]]
    _board = [deck[board[0]],deck[board[1]],deck[board[2]],deck[board[3]],deck[board[4]]]
    return showdown(_v1,_v2,_board)
    

    

board = ['Js','6h','3s','Jd','2d']
iterations = 1000000
#river(hero_test,vill_test,board,iterations)
river(hero_range,villain_range,board,iterations)
