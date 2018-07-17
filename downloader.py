import urllib.request
import os
import sys

def main():

	args = sys.argv

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