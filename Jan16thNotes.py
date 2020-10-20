#Eric Browne
def do_something():
    print("something")
def main():
    do_something()

if __name__ == '__main__':
    main()
#==============================================
#import sys as s
#from math import sin, cos


#print(s.argv)
#==========================
#CSV notes
import csv
with open('numbers.csv','r') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row[0])
with open("numbers.csv",'a') as f:
    writer = csv.writer(f)

    writer.writerow([5,6])
    writer.writerow([7,8])
#=============================================
#Classes notes
import unittest

class TestStringMethods(unittest.TestCase):



    def setUp(self):
        self.f = 'foo'
    def test_upper(self):
        self.assertEqual(self.f.upper(),'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse(self.f.isupper())
#Each test function is a single test TestCase

if __name__ == '__main__':
    unittest.main()
