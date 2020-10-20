# Eric Browne

#Python as a functional language
#imperative vs delclarative languages
#imperative =  what you explain the program to do step by step (most languages are like this)
#declarative = you say do something and the language figures it out  (SQL and other stuff)
#Procedural programming: lists of commands, not a lot of organization
#Object oriented language = what we are used to doing.
#       Java has to be object oriented, but python can be OO or Functional.  Python is more flexible
#Functional language = no variables, no objects, no state that changes as it goes
#       A lot easier to avoid bugs
#       A lot easer to write code, can break it down into pieces
############################################################################################
#Zip function
        # works like a zipper
        #combines multiple lists together
        #Outputs another list of tuples of the entries of the two lists
#Zip_longest
from the itertools module
        #if one list is longer than the other, if will fill in "None" values into the tuple entry
        #   for the smaller list
#############################################################################################
#Operator module
import operator

    #operator.gt = greater than
        #will generate a list of booleans for if one entry in a list is greater than another
from itertools import filterfalse
from itertools import starmap
from itertools import islice
from functools import partial
