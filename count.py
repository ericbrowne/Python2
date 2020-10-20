# Eric Browne Student ID: 873517924
# This program will count the frequency of characters in a given text file
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

        #Ouput in csv format
        for key,value in d.items():
            print("'" + key + "'," + str(value))


    #return d

def main():
    """Calls the add_frequency function, add applies additional flags"""
    boolean = True
    #initialize the command line flags
    commandC=False
    commandZ=False
    commandL=False
    commandVars=0
    numberFiles=0
    l_flag = 0

#Pass in the command line variables using the sys we imported
    for i in range(len(sys.argv)):
        if sys.argv[i] == "c":
            commandC = True
            commandVars+=1

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-z":
            commandZ=True
            commandVars+=1

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-l":
            commandL=True
            commandVars+=1
            letters = sys.argv[i+1]

    if commandL:
        l_flag=1

    #Next, create an empty dictionary (hardcode):
    for i in range(len(sys.argv)-commandVars-l_flag-1):
        print("-----------")
        d = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
        "A":0,
        "B":0,
        "C":0,
        "D":0,
        "E":0,
        "F":0,
        "G":0,
        "H":0,
        "I":0,
        "J":0,
        "K":0,
        "L":0,
        "M":0,
        "N":0,
        "O":0,
        "P":0,
        "Q":0,
        "R":0,
        "S":0,
        "T":0,
        "U":0,
        "V":0,
        "W":0,
        "X":0,
        "Y":0,
        "Z":0
        }
        #add_frequencies(d,sys.argv[i+1+commandVars+l_flag],commandC)

#Now lets go through all the different combinations of the flagged commands:

    # No flags used
    if ((not commandC) and (not commandZ) and (not commandL)):
        print(add_frequencies(dict,sys.argv[i+1+commandVars+l_flag],boolean))

    # Just -c flag
    if ((commandC) and (not commandZ) and (not commandL)):
        for key,value in d.items():
            print('"' + key + '",' + str(value))

    # Just -z flag
    if ((not commandC) and (commandZ) and (not commandL)):
        for key,value in d.items():
            if value!=0:
                print('"' + key + '",'+ str(value))
    #Just -l used
    if ((not commandC) and (not commandZ) and (commandL)):
        for key,value in d.items():
            if key in letters:
                print('"' + key + '",' + str(value))

    # -c annd -z, but not -l
    if ((commandC) and (commandZ) and (not commandL)):
        for key,value in d.items():
            if value!=0:
                print('"' + key +'",' + str(value))

    # -c and -l used, but not -z
    if (commandC) and (not commandZ) and (commandL):
        for key,value in d.items():
            if key in letters and value!= 0:
                print('"' + key + '",' + str(value))

    # All three flags are used
    if (commandC) and (commandZ) and (commandL):
        for key, value in d.items():
            if key in letters and value!=0:
                print('"'+key +'",'+str(value))
main()
