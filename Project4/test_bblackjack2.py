# Eric Browne StudentID#: 873517924
import unittest
import bblackjack2
import sys

class Testblackjack2(unittest.TestCase):
    def test_main(self):
        old_args = sys.argv

        try:
            sys.argv = ['', 1, 20]
            with self.assertRaises(TypeError):
                bblackjack2.main()

            sys.argv = ['', 0, 20, 'soft']
            with self.assertRaises(ValueError):
                bblackjack2.main()

            sys.argv = ['', 1, 21, 'soft']
            with self.assertRaises(ValueError):
                bblackjack2.main()

            sys.argv = ['', 1, 20, '']
            with self.assertRaises(ValueError):
                bblackjack2.main()
        finally:
            sys.argv = old_args

    # Now test for the stand function
    def test_stand(self):
        self.assertEqual(bblackjack2.stand(17, False, [11,1]), bblackjack2.Stand(True, 21))
        self.assertEqual(bblackjack2.stand(17, True, [1, 6]), bblackjack2.Stand(True, 17))
        self.assertFalse(bblackjack2.stand(17, False, [1, 6])), bblackjack2.Stand(False,17)
        self.assertTrue(bblackjack2.stand(17, False, [1, 6, 10])), bblackjack2.Stand(True,17)
        
    #Now test the score function
    def test_score(self):
        self.assertEqual(bblackjack2.score([ 3, 12 ]), bblackjack2.Score(13, 0))
        self.assertEqual(bblackjack2.score([ 5, 5, 10 ]), bblackjack2.Score(20, 0))
        self.assertEqual(bblackjack2.score([ 11, 10, 1 ]), bblackjack2.Score(21, 0))
        self.assertEqual(bblackjack2.score([ 1, 5 ]), bblackjack2.Score(16, 1))
        self.assertEqual(bblackjack2.score([ 1, 1, 5 ]), bblackjack2.Score(17, 1))
        self.assertEqual(bblackjack2.score([ 1, 1, 1, 7 ]), bblackjack2.Score(20, 1))
        self.assertEqual(bblackjack2.score([ 7, 8, 10 ]), bblackjack2.Score(25, 0))




if __name__ == '__main__':
    unittest.main()
