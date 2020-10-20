# Eric Browne Student ID: 873517924
#test_bbblackjack3, Project 5
#Python2: Software Development

'''This program test the bbblackjack3.py file!'''
import bblackjack3
import sys
import unittest

class Testbblackjack3(unittest.TestCase):

    def test_Strategy(self,stand_on_value, stand_on_soft,cards,expected_stand,expected_score):
        strat = bblackjack3.Strategy(stand_on_value,stand_on_soft)
        hand = bblackjack3.Hand(cards)
        (stand,score) = strat.stand(hand)
        self.assertEqual(stand,expected_stand)
        self.assertEqual(score,expected_score)

    def test_stand(self):
        self.test_strategy(17, False, [11,1],True, 21)
        self.test_strategy(17, True, [1,6],True, 17)
        self.test_strategy(17, False, [1,6],True, 17)
        self.test_strategy(17, False, [1,6,10],True, 17)

    def test_score(self):
        self.test_Hand([ 3, 12 ], bblackjack3.Score(13, 0), False,False)
        self.test_Hand([ 5, 5, 10 ], bblackjack3.Score(20, 0) ,False,False)
        self.test_Hand([ 10, 1 ], bblackjack3.Score(21, 0),False,True)
        self.test_Hand([ 11, 10, 1 ], bblackjack3.Score(21, 0),False,False)
        self.test_Hand([ 1, 5 ], bblackjack3.Score(16, 1),False,False)
        self.test_Hand([ 1, 1, 5 ], bblackjack3.Score(17, 1),False,False)
        self.test_Hand([ 1, 1, 1, 7 ], bblackjack3.Score(20, 1),False,False)
        self.test_Hand([ 7, 8, 10 ], bblackjack3.Score(25, 0),True,False)





    def test_Hand(self, cards, expectedScore, expectedBust, expectedBJ):
        hand = bblackjack3.Hand(cards)
        self.assertEqual(hand.score(), expectedScore)
        self.assertEqual(hand.is_bust(), expectedBust)
        self.assertEqual(hand.in_blackjack(), expectedBJ)

    def test_main(self):
        old_args = sys.argv
        try:
            sys.argv = ['', 1, 20]
            with self.assertRaises(TypeError):
                bblackjack3.main()

            sys.argv = ['', 0, 20, 'soft']
            with self.assertRaises(ValueError):
                bblackjack3.main()

            sys.argv = ['', 1, 21, 'soft']
            with self.assertRaises(ValueError):
                bblackjack3.main()

            sys.argv = ['', 1, 20, '']
            with self.assertRaises(ValueError):
                bblackjack3.main()
        finally:
            sys.argv = old_args

if __name__ == '__main__':
    unittest.main()
