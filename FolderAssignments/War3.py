"""
Name: Erika Price
Email: eprice1988@yahoo.com 
Assignment: Game of War
Due: 17 Feb 2017 @ 12:00 a.m.
"""


# -*- coding: utf-8 -*-

import os
import random

#Source: http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards

CARD = """\
┌───────┐
│{}     │
│       │
│   {}  │
│       │
│     {}│
└───────┘
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')

TEN = """\
┌───────┐
│{}    │
│       │
│   {}  │
│       │
│    {}│
└───────┘
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')

FACECARD = """\
┌───────┐
│{}│
│       │
│   {}  │
│       │
│{}│
└───────┘
""".format('{trank:<7}', '{suit: <2}', '{brank:>7}')

HIDDEN_CARD = """\
┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘
"""

class Card(object):
    
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """

        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]



        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10,
            'Ace': 11,  # value of the ace is high until it needs to be low
        }

        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': FACECARD,
            'Queen': FACECARD,
            'King': FACECARD,
            'Ace': FACECARD,  # value of the ace is high until it needs to be low
        }

        self.suits = ['Spades','Hearts','Diamonds','Clubs']

        self.symbols = {
            'Spades':   '♠',
            'Diamonds': '♦',
            'Hearts':   '♥',
            'Clubs':    '♣',
        }


        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit.capitalize()
        self.rank = str(rank)
        self.symbol = self.symbols[self.suit]
        self.points = self.card_values[str(rank)]
        self.ascii = self.__str__()
    

    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank+symbol
        brank = symbol+self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)
           
    def __cmp__(self,other):
        
        return self.ranks.index(self.rank) < self.ranks.index(other.rank) 
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)

###################################################################
"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]:
                self.cards.append(Card(suit,rank))

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "".join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def setup_hands(self, players):
        hands = [player.hand for player in players]
        while len(self.cards) >= len(players):
            for hand in hands:
                hand.add_card(self.cards.pop())
        return hands

###############################################################
class Hand:
    """
    For some reason I dont know why but the super() you had here was not working
    when I googled it said it was only compatable with python3 so I just changed it
    I did not feel comfortable enough with the super() to try and wing it.
    """
    def __init__(self, cards=None):
        """Initialize the class"""
        super().__init__()
        if (cards is not None):
            self._list = list(cards)
        else:
            self._list = []
    
    def __str__(self):
        return self.join_lines()

    def join_lines(self):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))

    def add_card(self, card):
        self._list.append(card)

    def take_top(self):
        return self._list.pop(0)

    #def add_all(self, cards):
        #self._list.extend(card)

    @property
    def has_cards(self):
        return bool (self._list)
        


#########################################################################

class Player:

    def __init__(self, name, hand):
        self.name, self.hand = name, hand

    def drop_card(self, collection):
        if self.hand.has_cards:
            collection.add_cards(self.hand.take_top(), self)
    
    def drop_bonus(self, collection, count):
        collection.add_bonus(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def give_cards(self,cards):
        self.hand.add_all(cards)

    def show_hand(self):
        print(self.name, 'has' , self.hand)

    
#########################################################################

class Pot:
    
    def __init__(self):
        self.cards = []
        self.players = []
        self.bonus = []

    def add_card(self, card, player):
        self.cards.append(card)
        self.players.append(player)

    def add_bonus(self, cards):
        self.bonus.extend(cards)

    @property
    def winner(self):
        self.show_pot()
        values = [card.value for card in self.cards]
        self.best = max(values)
        if values.count(self.best) == 1:
            return self.players[values.index(self.best)]

    def show_pot(self):
        for player, card in zip(self.players, self.cards):
            print('{} laid down a {}. ' .format(player.name, card))

    def reward(self, player):
        player.give_cards(self.cards)
        player.give_cards(self.bonus)

    @property
    def tied(self):
        for card, player in zip(self.cards, self.players):
            if card.value == self.best:
                yield player

########################################################################

class Table:
    
    def __init__(self, players):
        self.players = [Player(name, Hand()) for name in players]
        self.deck = Deck()
        self.rounds = 0

    def deal_cards(self):
        self.deck.shuffle()
        self.deck.setup_hands(self.players)
        for players in self.players:
            players.show_hand()

    def count_rounds(self):
        self.rounds += 1
        print('Starting round {}' .format(self.rounds), '=')
    
    def play_once(self, tied = None):
        if tied is None:
            self.count_rounds()
        collection = Pot()
        for player in (self.players if tied is None else tied):
            player.drop_card(collection)
            if tied:
                player.drop_bonus(collection, 3)
            winner = collection.winner
            if winner is not None:
                collection.reward(winner)
            else:
                winner = self.play_once(collection.tied)
                collection.reward(winner)
            return winner

    def play_all(self):
        while not self.finished:
            self.play_once()
        self.show_winner()

    def show_winner(self):
        for player in self.players:
            if player.hand.has_cards:
                print()
                print(player.name, 'Wins!!')
                break
    @property
    def finished(self):
        return sum(bool(player.hand.cards) for player in self.players) == 1

####################################################################################

def main():
    table = Table(['Dealer', 'Player 1'])
    table.deal_cards()
    table.play_all()


####################################################################################
if __name__ == '__main__':
    main()
