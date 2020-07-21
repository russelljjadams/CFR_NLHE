# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:18:24 2017

@author: GWF2-Guest
"""

import random
from PokerPlayer import PokerPlayer
from PokerEval import showdown
from Deck import r_deck



class PokerDealer:
    def __init__(self,bb,sb):
        self.players = 0
        self.players_list = {}
        self.button_seat = 0
        self.small_blind_seat = 1
        self.big_blind_seat = 2
        self.small_blind = sb
        self.big_blind = bb
        self.deck = None
        self.pot = 0
        self.street_actions = [self.big_blind_seat, self.button_seat, self.button_seat, self.button_seat]
        self.street = 0
        self.board = []
    
    def sit_player(self, buy_in, human=False):
        self.players_list[self.players] = PokerPlayer(self.players, buy_in, human)
        self.players += 1
        
    def set_blinds(self):
        if self.players == 2:
            self.small_blind_seat = self.button_seat
            self.big_blind_seat = (self.button_seat + 1) % self.players
        else:
            self.small_blind_seat = (self.button_seat + 1) % self.players
            self.big_blind_seat = (self.button_seat + 2) % self.players

    def get_blinds(self):
        self.pot = self.small_blind + self.big_blind
        self.players_list[self.small_blind_seat].post_blind(self.small_blind)
        self.players_list[self.big_blind_seat].post_blind(self.big_blind)
        
    def move_button(self):
        self.button_seat = (self.button_seat + 1) % self.players
        
    def new_deck_shuffle(self):
        self.deck = range(1,53)
        random.shuffle(self.deck)

    def deal_hole_cards(self):
        current_deal = self.small_blind_seat
        for i in range(2):
            for j in range(self.players):
                self.players_list[current_deal].get_card(self.deck.pop())
                current_deal = (current_deal + 1) % self.players

    def player_actions(self):
        next_to_act = (self.street_actions[self.street] + 1) % self.players
        all_acted = False
        while not all_acted:
            self.pot += self.players_list[next_to_act].act() #Actual Call to the Player.Act() function.
            print self.get_board()
            next_to_act = (next_to_act + 1) % self.players
            all_acted = all([player.acted for player in self.players_list.itervalues()])
        if all([player.has_folded() for player in self.players_list.itervalues()]):
            return
        self.next_street()
            
    def next_street(self):
        self.street += 1
        if self.street == 4:
            return self.get_showdown_two()
        elif self.street == 1:
            self.deal_flop()
        else:
            self.deal_one()
        for p in range(self.players):
            if not self.players_list[p].has_folded():
                self.players_list[p].action_change()
        self.player_actions()
                
    def deal_flop(self):
        for i in range(3):
            self.board.append(self.deck.pop())
            
    def deal_one(self):
        self.board.append(self.deck.pop())
        
    def get_showdown_two(self):
        p1, p2 = self.players_list[0], self.players_list[1]
        winner = showdown(self.players_list[0].print_hand(False),self.players_list[1].print_hand(False),self.board)
        if winner:
            p1.add_won(self.pot)
        else:
            p2.add_won(self.pot)
        
    def get_board(self):
        board = []
        for i in self.board:
            board.append(r_deck[i])
        return board

    def new_hand(self):
        self.street = 0
        self.board = []
        for i in range(self.players):
            self.players_list[i].begin_new_turn()
        self.move_button()
        self.set_blinds()
        self.get_blinds()
        self.new_deck_shuffle()
        self.deal_hole_cards()
        self.player_actions()

p = PokerDealer(1,3)
p.sit_player(300,True)
p.sit_player(300)
p.new_hand()

        
    