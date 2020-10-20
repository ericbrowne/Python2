# Eric Browne Student ID: 873517924
# This program outputs a csv file, with the counts of characters from
#other input files.

# First, lets import a bunch of modules,
#including our original count.py module.
import sys
import countanswer
import string
import count


outfile = sys.argv[-1]
del sys.argv[-1]  #get rid of the file name, since we dont need that lol

# First, lets modulize the main function from the first count.py
def main2():
	return count.main()

def writeFiles(name,content):
	f = open(name,"w")
	f.write(content)
	f.close()

def csv_format1(frequencies):
	s = " " #initialize an empty string
	for key in frequencies:
		if (key not in string.ascii_letters):
			continue
		val = frequencies[key]
		s += key + "," + str(val) + "\n"
	return s

#call the main2(), which calls main() from the count.py solution
frequencies = main2()
writeFiles(outfile,csv_format1(frequencies))
#print(frequencies)
