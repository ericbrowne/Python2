# ==============================
# NAME
# DATE
# CLASS
# HOMEWORK NUMBER
# PROGRAM DESCRIPTION
# ==============================

import sys

# ==============================================
# Beginning of the ADD FREQUENCIES function
# ==============================================
def add_frequencies(d,file,remove_case):

	f = open(file)
	my_file_data=f.read()
	string_length=len(my_file_data)


	if remove_case == False:
		for jj in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
			for i in range(string_length-1):
				if my_file_data[i] ==  jj:
					d.update({jj: d.get(jj)+1})


	if remove_case == True:
		for jj in "abcdefghijklmnopqrstuvwxyz":
			for i in range(string_length-1):
				if my_file_data[i] == jj or my_file_data[i] == jj.upper():
					d.update({jj: d.get(jj)+1})

# ==============================================
# End of the ADD FREQUENCIES function
# ==============================================


# ==============================================
# Beginning of the MAIN function
# ==============================================

def main():

# ==============================================
# Set all command line variable to False
# ==============================================
	cmd_c=False
	cmd_z=False
	cmd_l=False
	cmd_variables=0
	number_of_files=0
	l_flag=0

# ==============================================
# Parse command line variables
# ==============================================
	for x in range(len(sys.argv)):
		if sys.argv[x] == "-c":
			cmd_c=True
			cmd_variables=cmd_variables+1

	for x in range(len(sys.argv)):
		if sys.argv[x] == "-z":
			cmd_z=True
			cmd_variables=cmd_variables+1


	for x in range(len(sys.argv)):
		if sys.argv[x] == "-l":
			cmd_l=True
			cmd_variables=cmd_variables+1
			letters=sys.argv[x+1]

	if cmd_l:
		l_flag=1
	for x in range(len(sys.argv)-cmd_variables-l_flag-1):
		print("=================================")
# ==============================================
# Create EMPTY DICTIONARY
# ==============================================
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
		"A": 0,
		"B": 0,
		"C": 0,
		"D": 0,
		"E": 0,
		"F": 0,
		"G": 0,
		"H": 0,
		"I": 0,
		"J": 0,
		"K": 0,
		"L": 0,
		"M": 0,
		"N": 0,
		"O": 0,
		"P": 0,
		"Q": 0,
		"R": 0,
		"S": 0,
		"T": 0,
		"U": 0,
		"V": 0,
		"W": 0,
		"X": 0,
		"Y": 0,
		"Z": 0
		}

		add_frequencies(d,sys.argv[x+1+cmd_variables+l_flag],cmd_c)

# ==============================================
# Printing appropriate output
# ==============================================
		if ((not cmd_c) and (not cmd_z) and (not cmd_l)):
			for key, value in d.items():
				print('"' + key + '",' + str(value))

		if ((cmd_c) and (not cmd_z) and (not cmd_l)):
			for key, value in d.items():
				print('"' + key + '",' + str(value))

		if ((not cmd_c) and (cmd_z) and (not cmd_l)):
			for key, value in d.items():
				if value != 0:
					print('"' + key + '",' + str(value))

		if ((cmd_c) and (cmd_z) and (not cmd_l)):
			for key, value in d.items():
				if value != 0:
					print('"' + key + '",' + str(value))

		if ((not cmd_c) and (not cmd_z) and (cmd_l)):
			for key, value in d.items():
				if key in letters:
					print('"' + key + '",' + str(value))

		if ((cmd_c) and (not cmd_z) and (cmd_l)):
			for key, value in d.items():
				if key in letters:
					print('"' + key + '",' + str(value))

		if ((not cmd_c) and (cmd_z) and (cmd_l)):
			for key, value in d.items():
				if key in letters and value != 0:
					print('"' + key + '",' + str(value))

		if ((cmd_c) and (cmd_z) and (cmd_l)):
			for key, value in d.items():
				if key in letters and value != 0:
					print('"' + key + '",' + str(value))


main()
