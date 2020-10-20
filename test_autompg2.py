import unittest
from autompg2 import AutoMPG
import requests


class TestAutoMPG(unittest.TestCase):

    def setUp(self):
        self.auto1 = AutoMPG('Honda', 'Civic', 2007, 45.1)
        self.auto2 = AutoMPG('Honda', 'Civic', 2007, 45)
        self.auto3 = AutoMPG('Honda', 'Civic', 2006, 45)
        self.auto4 = AutoMPG('Honda', 'Odyssey', 2000, 20)
        self.auto5 = AutoMPG('Toyota', 'Sienna', 2012, 46)
        self.auto6 = AutoMPG('Honda', 'Civic', 2007, 45.1)

    def test_auto_mpg(self):
        self.assertEqual(self.auto1.make, 'Honda')
        self.assertEqual(self.auto1.model, 'Civic')
        self.assertEqual(self.auto1.year, 2007)
        self.assertEqual(self.auto1.mpg, 45.1)

    def test_equal(self):
        self.assertEqual(self.auto1, self.auto6)
        self.assertNotEqual(self.auto1, self.auto2)

    def test_lt(self):
        self.assertTrue(self.auto1 > self.auto2)
        self.assertTrue(self.auto2 > self.auto3)
        self.assertTrue(self.auto3 < self.auto4)
        self.assertTrue(self.auto5 > self.auto4)
        self.assertFalse(self.auto1 < self.auto6)
        self.assertFalse(self.auto1 > self.auto6)

    def test_hash(self):
        self.assertEqual(hash(self.auto1), hash(self.auto6))
        self.assertNotEqual(hash(self.auto1), hash(self.auto2))

if __name__ == '__main__':
    unittest.main()
