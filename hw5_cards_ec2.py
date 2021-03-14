import random
import unittest
 
class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order 
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}
 

    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)
 
    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"
 

class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self): 

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order
 
    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i) 
 
    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)
 
    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list
    
    def sort_cards(self):
        '''returns the Deck to its original order
        
        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
 
    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, num_hands, num_cards_per_hand=-1):
        ''' deal deck to hands, each hands have the same number of cards(num_cards_per_hand), if the num_cards_per_hand is set -1, then all cards will be dealt. If 52 cannot be divided evenly by num_hands, then one of the players will have one more card.

            the result of (num_hands * num_cards_per_hand) should be less than 52.

            this function will deal as fair as possible. For example if there are 5 players and deal all the cards, then they will have 10,10,10,11,11 cards respectively, instead of 11,11,11,11,8 cards respectively.
            Parameters  
            -------------------
            num_hands: int
                the number of players
            num_cards_per_hand:
                the number of cards per player. default value is -1

            Returns
            -------
            list
                a list of hands (players)
        '''
        hand_list = []
        if num_cards_per_hand > 0:
            for i in range(0, num_hands):
                hand_list.append(Hand(self.deal_hand(num_cards_per_hand)))
        else:
            num_cards = 52//num_hands
            mod = 52%num_hands
            for i in range(0, num_hands):
                if (mod == 0):
                    hand_list.append(Hand(self.deal_hand(num_cards)))
                else:
                    hand_list.append(Hand(self.deal_hand(num_cards+1)))
                    mod -= 1

        return hand_list

def print_hand(hand):
    '''prints a hand in a compact form
    
    Parameters  
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)

class Hand:

    def __init__(self, init_cards):
        self.cards = init_cards

    def add_card(self, card):
        already_in = 0
        for init_card in self.cards:
            if (init_card.__str__() == card.__str__()):
                print('Add card Failed! Card is already in the hand!')
                already_in = 1
                break
        if (not already_in):
            self.cards.append(card)

    def remove_card(self, card):
        for init_card in self.cards:
            if (init_card.__str__() == card.__str__()):
                self.cards.remove(init_card)
                return card
        return None

    def draw(self, deck):
        card = deck.deal_card(random.randint(0,len(deck.cards)))
        self.add_card(card)

    def remove_pairs(self):
        '''
            remove pairs of cards in a hand (remove 2/4 same rank cards and keep 3 same rank cards)
        '''
        rank_list = []
        for card in self.cards:
            rank_list.append(card.rank)
        index_list = []
        for index in range(len(rank_list)):
            if rank_list.count(rank_list[index]) == 2 or rank_list.count(rank_list[index]) == 4:
                pass
            else:
                index_list.append(index)
        final_list = []
        for index in index_list:
            final_list.append(self.cards[index])
        self.cards = final_list