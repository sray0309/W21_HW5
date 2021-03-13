import random, unittest
import hw5_cards
import hw5_cards_ec1

class TestHand(unittest.TestCase):

    def test1_init(self):
        d = hw5_cards.Deck() # create a deck
        d.shuffle() # shuffle the deck
        hand_size = random.randint(1,52) # generate a random hand size
        hand = d.deal_hand(hand_size) # create a temp hand list from deck also update the deck
        h = hw5_cards_ec1.Hand(hand) # create hand object
        for i in range(0,hand_size):
            self.assertEqual(h.init_cards[i].__str__(), hand[i].__str__())

    def test2_AddAndRemove(self):
        d = hw5_cards.Deck() # create a deck
        d.shuffle() # shuffle the deck
        hand_size = random.randint(1,52) # generate a random hand size
        hand = d.deal_hand(hand_size) # create a temp hand list from deck also update the deck
        h = hw5_cards_ec1.Hand(hand) # create hand object
        num_cards_in_hand = len(h.init_cards) # how many cards in the hand now
        c_new = d.deal_card() # create a card in the deck but not in the hand
        c_old = h.init_cards[random.randint(0,len(h.init_cards))] # create a card in the hand but not in the deck
        h.add_card(c_old)
        self.assertEqual(len(h.init_cards), num_cards_in_hand)
        h.add_card(c_new)
        self.assertEqual(len(h.init_cards), num_cards_in_hand+1)
        h.remove_card(c_new)
        self.assertEqual(len(h.init_cards), num_cards_in_hand)
        h.remove_card(c_old)
        self.assertEqual(len(h.init_cards), num_cards_in_hand-1)

    def test3_draw(self):
        d = hw5_cards.Deck() # create a deck
        d.shuffle() # shuffle the deck
        hand_size = random.randint(1,52) # generate a random hand size
        hand = d.deal_hand(hand_size) # create a temp hand list from deck also update the deck
        h = hw5_cards_ec1.Hand(hand) # create hand object
        num_cards_in_hand = len(h.init_cards) # how many cards in the hand now
        num_cards_in_dect = len(d.cards) # how many cards in the dect now
        h.draw(d)
        self.assertEqual(len(h.init_cards), num_cards_in_hand+1)
        self.assertEqual(len(d.cards), num_cards_in_dect-1)
        h.draw(d)
        self.assertEqual(len(h.init_cards), num_cards_in_hand+2)
        self.assertEqual(len(d.cards), num_cards_in_dect-2)

if __name__=="__main__":
    unittest.main()