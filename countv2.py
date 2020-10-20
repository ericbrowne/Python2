# Eric Browne Student ID: 873517924
# This program will count the frequency of characters in a given text file(s) that you manually enter on the command line!
from string import ascii_lowercase
from string import ascii_uppercase
import sys

#Initialize a dictionary
dict = {}
def add_frequencies(d,file,remove_case):
    """ adds the amount of times a character occurs in a text file"""
    #remove_case = false: ascii_uppercase
    #remove_case = true: ascii_lowercase
    with open(file) as f:
        text = f.read().strip('\n')
        print(text)
        dict = {} #initialize dictionary
        list = [] #Initialize list for later
        if remove_case == False:
            for i in text:
                if i in ascii_uppercase or ascii_lowercase:
                    d[i] = text.count(i)
        if remove_case == True:
            for i in text:
                if i in ascii_lowercase or ascii_uppercase:
                    list += [i.lower()] #list comprehension to make a list of the lower case letters
            for i in list:
                d[i] = list.count(i)

    return d

def main():
	"""Calls add_frequencies, but also uses additional flags"""
	cmdC=False
	cmdZ=False
	cmdL=False
	boolean=True
	cmdVariables=0
	number_of_files=0
	l_flag=0

#Pass in the command line variables using the sys we imported
	for i in range(len(sys.argv)):
		if sys.argv[i] == "-c":
			cmdC=True
			cmdVariables+=1

	for i in range(len(sys.argv)):
		if sys.argv[i] == "-z":
			cmdZ=True
			cmdVariables+=1


	for i in range(len(sys.argv)):
		if sys.argv[i] == "-l":
			cmdL=True
			cmdVariables+=1
			letters=sys.argv[i+1]

	if cmdL:
		l_flag=1
	for i in range(len(sys.argv)-cmdVariables-l_flag-1):
# hardcode a dictionary to use
		d = {
		"a": 0,
		"b": 0,
		"c": 0,
		"d": 0,
		"e": 0,
		"f": 0,
		"g": 0,
		"h": 0,
		"i": 0,
		"j": 0,
		"k": 0,
		"l": 0,
		"m": 0,
		"n": 0,
		"o": 0,
		"p": 0,
		"q": 0,
		"r": 0,
		"s": 0,
		"t": 0,
		"u": 0,
		"v": 0,
		"w": 0,
		"x": 0,
		"y": 0,
		"z": 0,

		}

		add_frequencies(d,sys.argv[i+1+cmdVariables+l_flag],cmdC)


# Printing the different outputs for the given flags on the command line

# No flags at all
		if ((not cmdC) and (not cmdZ) and (not cmdL)):
			for key, value in d.items():
				if value!=0:
					print('"' + key + '",' + str(value))

# only the -z flag
		if ((cmdZ) and (not cmdC) and (not cmdL)):
			for key, value in d.items():
				if value!=0:
					print('"' + key + '",' + str(value))

#only the -c flag
		if ((not cmdZ) and (cmdC) and (not cmdL)):
			for key, value in d.items():
				if value != 0:
					print('"' + key + '",' + str(value))
#Only -l flag
		if ((not cmdZ) and (not cmdC) and (cmdL)):
			for key, value in d.items():
				if key in letters:
					print('"' + key + '",' + str(value))

#-z and -c flag
		if ((cmdZ) and (cmdC) and (not cmdL)):
			for key, value in d.items():
				if value != 0:
					print('"' + key + '",' + str(value))

#-z and -l flags
		if ((cmdZ) and (not cmdC) and (cmdL)):
			for key, value in d.items():
				if key in letters:
					print('"' + key + '",' + str(value))

#-c and -l flags
		if ((not cmdZ) and (cmdC) and (cmdL)):
			for key, value in d.items():
				if key in letters and value != 0:
					print('"' + key + '",' + str(value))

#All the flags
		if ((cmdZ) and (cmdC) and (cmdL)):
			for key, value in d.items():
				if key in letters and value != 0:
					print('"' + key + '",' + str(value))
					
main() #execute main function
