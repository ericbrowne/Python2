# Eric Browne Student ID#: 873917524
#This code will be to test the blackjack.py script
import unittest
import blackjack

class TestBlackjack(unittest.TestCase):
    def test_get_card(self):
        self.assertIn(blackjack.get_card(),set(range(1,14)))

    def test_score(self):
        self.assertEqual(blackjack.score([3,12]), (13,0))
        self.assertEqual(blackjack.score([5,5,10]), (20,0))
        self.assertEqual(blackjack.score([11,10,1]), (21,0))
        self.assertEqual(blackjack.score([1,5]), (16,1))
        self.assertEqual(blackjack.score([1,1,5]), (17,1))
        self.assertEqual(blackjack.score([1,1,1,7]), (20,1))
        self.assertEqual(blackjack.score([7,8,10]), (25,0))

    def test_stand(self):
        # total > stand stand on value
        self.assertTrue(blackjack.stand(17,True,[10,5,3]))
        self.assertTrue(blackjack.stand(17,False,[10,5,3]))
        #total < stand on value
        self.assertFalse(blackjack.stand(17,True,[10,5]))
        self.assertFalse(blackjack.stand(17,False,[10,5]))
        #total == stand on value
        self.assertTrue(blackjack.stand(17,True,[10,5,1,1]))  #with aces
        self.assertFalse(blackjack.stand(17,False,[10,5,1,1])) #with aces
        self.assertTrue(blackjack.stand(17,True,[10,5,2])) #no aces
        self.assertFalse(blackjack.stand(17,False,[10,5,2])) #no aces

if __name__ == '__main__':
    unittest.main()
