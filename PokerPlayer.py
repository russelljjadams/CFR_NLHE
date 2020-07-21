# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 04:17:33 2017

@author: 4bet20x
"""

import random
from Deck import r_deck

class PokerPlayer:
    def __init__(self, serial, money, human=False):
        self.rebuy = money
        self.serial = serial
        self.money = money
        self.bet = 0
        self.fold = False
        self.hand = []
        self.acted = False
        self.action_history = []
        self.human = human
        
    def begin_new_turn(self):
        self.bet = 0
        self.fold = False
        self.hand = []
        self.has_acted = False
        self.action_history = []

    def post_blind(self, blind):
        self.money -= blind
        
    def get_money(self):
        return self.money

    def get_card(self,card):
        self.hand.append(card)
        
    def get_serial(self):
        return self.serial
        
    def rebuy(self):
        self.money = self.rebuy

    def has_acted(self):
        return self.acted

    def action_change(self):
        self.acted = [True, False][self.acted]
    
    def has_folded(self):
        return self.fold
        
    def fold(self):
        self.fold = True
        self.acted = True
        
    def check(self):
        self.acted = True
        
    def bet(self, current_pot):
        self.acted = True
        self.money -= amount
        self.bet = amount
        
    def get_bet(self):
        return self.bet
        
    def add_won(self, amount):
        self.money += amount
        
    def get_history(self):
        return self.action_history
        
    def new_action(self,action):
        self.action_history.append(action)
        
    def print_hand(self, readable=True):
        if readable:
            return r_deck[self.hand[0]], r_deck[self.hand[1]]
        else:
            return self.hand
        
    def act(self):
        if self.human:
            self.human_play()
        self.action_change()
        return 0
    
    def human_play(self):
        print self.print_hand()
        
        