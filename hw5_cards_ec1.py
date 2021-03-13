import hw5_cards
import random

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
        card = deck.deal_card(random.randint(0,len(deck.cards)-1))
        self.add_card(card)


