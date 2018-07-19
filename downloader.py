import urllib.request
import os
import sys

def main():

	args = sys.argv

	if len(args) != 3:
		print("Invalid arguments... Please provide the file with the list of images as the first argument and the base name for the output file as the second argument.")
		return

	input_name = args[1]
	base_name = args[2]

	file = open(input_name,"r")
	urls = file.readlines()

	createFolder("./pics/")

	x = 1
	for url in urls:
		resource = None;
		output_name = "pics/" + base_name + "_" + str(x) + ".jpg"
		try:
			resource = urllib.request.urlopen(url)
			output = open(output_name,"wb")
			output.write(resource.read())
			output.close()
			x+=1
		except Exception as e:
			print ("Can't find requested image.")
	file.close()

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == "__main__":
    main()