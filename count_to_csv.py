# Eric Browne Student ID: 873517924
#This code will import count.py, and print it to a CSV file

import sys
#    For this homework assignment, my original count.py printed out the wrong results from the different flags,
#and i couldn't figure out how to switch them to output the correct dictionary.
#    So, i imported the sample answer that you provided on canvas to run this homework assignment.
import countanswer
import csv
import sys
outfile = sys.argv[-1]
del sys.argv[-1]

import countanswer
import string

def main2():
	return countanswer.main()

def writeFile(name,content):
	f = open(name,"w")
	f.write(content)
	f.close()

def csv_format(freqs):
	s = " "

	for key in freqs:
		if (key not in string.ascii_letters):
			continue

		val = freqs[key]

		s += key + "," + str(val) + "\n"

	return s
freqs = main2()

print(freqs)
writefile(outfile,csv_format(freqs))
