import random, unittest
import hw5_cards_ec2

class Testec2(unittest.TestCase):

    def test1(self):
        d = hw5_cards_ec2.Deck() # create a deck
        d.shuffle() # shuffle the deck
        hand_size = random.randint(1,51) # generate a random hand size
        hand = d.deal_hand(hand_size) # create a temp hand list from deck also update the deck
        h = hw5_cards_ec2.Hand(hand) # create hand object 
        h.remove_pairs() # remove pairs in this hand
        card_list = [i.rank for i in h.cards] # create a list of rank
        for rank in card_list:
            self.assertFalse(card_list.count(rank)==2)
            self.assertFalse(card_list.count(rank)==4)

    def test2(self):
        d1 = hw5_cards_ec2.Deck() # create a deck for test num_cards_per_hand is not -1
        d1.shuffle() # shuffle the deck
        d2 = hw5_cards_ec2.Deck() # create a deck for test num_cards_per_hand is -1
        d2.shuffle() # shuffle the deck
        num_hands = random.randint(1,51)

        # test num_cards_per_hand is not -1
        num_cards = random.randint(1,52//num_hands)
        hand_list = d1.deal(num_hands, num_cards)
        for i in hand_list:
            self.assertEqual(len(i.cards),num_cards)

        # test num_cards_per_hand is -1
        num_cards = 52//num_hands
        hand_list = d2.deal(num_hands)
        for i in hand_list:
            self.assertTrue(len(i.cards) in [num_cards, num_cards+1]) 



if __name__=="__main__":
    unittest.main()