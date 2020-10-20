# Eric Browne Student ID: 873517924
"""
This Progam called test_count.py. This Program contains the
unit testing code for count.py (count.py is a program
provided as a solution-problem for the assignment 1, count.py was
mainly writtenby Max Roschke. I did make small modifications for
the purpose of the excercise.
This progtams tests every combination of flags.
"""
import os
import sys
import string
import count



def writeFile(name,content):
	f = open(name,"w")
	f.write(content)
	f.close()

def runTest(test):
	'''Apply test args and run program'''
	print("------Running Test: " + test["name"] + "---------")

	sys.argv = test["args"]
	result = test["functionToRun"]()
	#print(result)
	error = False

	for key in test["expected"]:
		if key not in result:
			print("error:expected key " + key + " not in result")
			error = True
			continue

		val = result[key]
		expectedVa1 = test["expected"][key]

		if val != expectedVa1:
			error = True
			print("error: key " + key + " was" + str(val) + " , expected " + str(expectedVa1))

	if error:
		print("Test , " + test["name"] + " Failed")
	else:
		print("Test , " + test["name"] + " Passed")
# set up some data
testData = "AA bb Cc dD"
writeFile("__data.txt",testData)

#set up some test args
plaintest = {
	'name': "No-flags",
	'args':["testing","__data.txt"],
	'expected': {"a": 2, "b":2, "c":2, "d":2 },
	'functionToRun': count.main
}
casetest = {
	'name': "'-c' 'flag-only'",
	'args':["testing", "-c", "__data.txt"],
	'expected': { "A":2, "b":2,"c":1,"C":1,"D":1,"d":1},
	'functionToRun': count.main
}
casezerotest = {
	'name': "'z' and 'c' flags",
	'args':["testing", "-z", "-c", "__data.txt"],
	'expected': { "A":2, "b":2,"c":1,"C":1,"D":1,"d":1},
	'functionToRun': count.main
}
letterstest = {
	'name': "'-l ab' flag only",
	'args':["testing", "-l", "ab","__data.txt"],
	'expected': {"a":2,"b":2},
	'functionToRun': count.main
}
caseletterstest = {
	'name': "'-c' and '-l ab' flags",
	'args':["testing", "-c", "-l", "ab","__data.txt"],
	'expected': {"b":2},
	'functionToRun': count.main
}
alltest = {
	'name': "'-z' '-c' and '-l ab' flags",
	'args':["testing", "-z", "-c", "-l", "ab","__data.txt"],
	'expected': {"b":2},
	'functionToRun': count.main
}
casetest_z_only = {
	'name': "'-z' 'flag-only'",
	'args':["testing", "-z", "__data.txt"],
	'expected': {"a":2,"b":2,"c":2,"d":2}, #expected has non-zeros values since count.py already checked that
	'functionToRun': count.main
}
case_z_l_only = {
	'name': "'-z' and '-l abbc' flags",
	'args':["testing", "-z", "-l", "abcd","__data.txt"],
	'expected': {"a":2,"b":2,"c":2,"d":2},
	'functionToRun': count.main
}
runTest(plaintest)
runTest(casetest)
runTest(casezerotest)
runTest(letterstest)
runTest(caseletterstest)
runTest(alltest)
runTest(casetest_z_only)
runTest(case_z_l_only)

os.remove("__data.txt")   #remove file, no need any more.
