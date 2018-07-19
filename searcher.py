import os
import sys

def main(): 

	args = sys.argv

	if len(args) != 3:
		print("Invalid arguments... Please provide the word you are searching for as the first command line argument and the amount of XML files you are looking through as the second argument.")
		return

	word = args[1].lower()
	print("Looking for \"" + word + "\"...")

	num_files = 0

	try:
		num_files = int(args[2])
	except Exception as e:
		print("Invalid second argument... Please provide the second command line argument as a valid integer.")
		return

	found = False

	for x in range(0, num_files):

	    input_name = "xml/" + str(x) + ".xml"

	    try:
	    	file = open(input_name,"r")
	    except Exception as e:
	    	# print("File " + input_name + " is not present.")
	    	continue

	    # print("File " + input_name + " is present.")

	    data = file.read().replace('\n', '').lower()

	    if word in data:
	    	print("The word \"" + word + "\" is present in " + input_name)
	    	found = True

	if not found:
		print("The word \"" + word + "\" was not found in any of the files.")

if __name__ == "__main__":
    main()