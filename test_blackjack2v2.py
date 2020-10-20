# Eric Browne
import unittest
import blackjack2v2
import sys

class Testblackjack2v2(unittest.TestCase):

    def test_score(self):
        self.assertEqual(blackjack2v2.score([ 3, 12 ]), (13, 0))
        self.assertEqual(blackjack2v2.score([ 5, 5, 10 ]), (20, 0))
        self.assertEqual(blackjack2v2.score([ 11, 10, 1 ]), (21, 0))
        self.assertEqual(blackjack2v2.score([ 1, 5 ]), (16, 1))
        self.assertEqual(blackjack2v2.score([ 1, 1, 5 ]), (17, 1))
        self.assertEqual(blackjack2v2.score([ 1, 1, 1, 7 ]), (20, 1))
        self.assertEqual(blackjack2v2.score([ 7, 8, 10 ]), (25, 0))

    def test_stand(self):
        self.assertEqual(blackjack2v2.stand(21, True, [11,1]),blackjack2v2.Stand(True,21))
        self.assertEqual(blackjack2v2.stand(17, True, [1,6]),blackjack2v2.Stand(True,17))
        self.assertEqual(blackjack2v2.stand(17, False, [1,6]),blackjack2v2.Stand(False,17))
        self.assertEqual(blackjack2v2.stand(17, False, [1,6,10]),blackjack2v2.Stand(True,17))

    def test_main(self):
        old_args = sys.argv

        try:
            sys.argv = ['', 1, 20]
            with self.assertRaises(TypeError):
                blackjack2v2.main()

            sys.argv = ['', 0, 20, 'soft']
            with self.assertRaises(ValueError):
                blackjack2v2.main()

            sys.argv = ['', 1, 21, 'soft']
            with self.assertRaises(ValueError):
                blackjack2v2.main()

            sys.argv = ['', 1, 20, '']
            with self.assertRaises(ValueError):
                blackjack2v2.main()
        finally:
            sys.argv = old_args

if __name__ == '__main__':
    unittest.main()

def old_main():
    '''Runs the specified number of blackjack simulations using the specified
    strategy and prints out the percentage of time the hand busted.
    Usage: blackjack.py <num-simulations> <stand-on-value (1-20)> <'soft'|'hard'>
    '''
    args = sys.argv[1:]

    #print(stand(17, False, [1,6,10]))   #clean
    print(play_hand(17, False))
    return                          #clean

    if len(args) != 3:
        print(main.__doc__, file = sys.stderr)
        raise TypeError

    num_simulations = int(args[0])
    stand_on_value = int(args[1])

    if(num_simulations < 1):
        raise ValueError(f'Invalid number of simulations: {num_simulations}. num_simulations must be positive.')

    if(stand_on_value > 20 or stand_on_value < 1):
        raise ValueError(f'Invalid stand on value: {stand_on_value}. Value values are 1-20.')

    if(args[2] != 'soft' and args[2] != 'hard'):
        print(main.__doc__, file = sys.stderr)
        raise ValueError(f'Unknown argument: {args[2]}')

    stand_on_soft = args[2] == 'soft'
    bust_count = 0

    for i in range(0, num_simulations):
        cards = [get_card(), get_card()]

        while not stand(stand_on_value, stand_on_soft, cards):
            cards.append(get_card())
            new_score = score(cards)
            bust_count += new_score[0] > 21

    print(bust_count/num_simulations)
