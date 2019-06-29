"""
'Python-is-Easy' Homework #8 (Input and Output)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with Input and Output (I/O) in Python.  It is the eighth homework assigment in the
'Python is Easy' course, from Pirple.

Create a note taking application that creates a new file (if it doesn't exist), save the file as named by the user and the contents of the text input by the user, saved into the file.  
If the file already exists, the application should present options to amend, edit or read the file. 


 
"""
Filename = input("Please enter a file name: ")


import os
existingFiles = os.listdir(".")

newlist = []

print(existingFiles)

if str(Filename)+".txt" not in existingFiles:
	File = open(str(Filename) + ".txt","w")
	File.write(input("Compose the contents of your new file:\n"))
	File.close()

else:
	userOption = input("\nFile already exists.  What would you like to do? \n\n1) Read the file\n2) Delete the File and Start Over\n3) Append the file\n4) Replace a single line in the file\n\n<<CHOOSE AN OPTION ABOVE>>\n")
	if userOption == "1":
		File = open(str(Filename) + ".txt","r")
		for line in File:
			print(line)
		File.close()
	if userOption == "2":
		File = open(str(Filename) + ".txt","w")
		File.write(input("Compose the new contents of your file:\n"))
		File.close()
	if userOption == "3":
		appendedText = input("Compose text to add to the file:\n")
		File = open(str(Filename) + ".txt","a")
		File.write("\n"+str(appendedText))
		File.close()
	if userOption == "4":
		File = open(str(Filename) + ".txt","r")
		numLines = sum(1 for l in File)
		# print(numLines)
		File.close()
		File = open(str(Filename) + ".txt","r")
		print("=========== EDIT FILE ============")
		for p in range(numLines):
			fileLines = File.readline()
			print("Line",int(p)+1," >> ",fileLines,end="")
		File.close()
		print("\n==================================")
		lineSelect = input("\nWhich line would like to change?\nLine number: ")
		newTextLine = input("\nCompose the new text:\n")
		File = open(str(Filename) + ".txt","r")
		fileLineData = File.readlines()
		fileLineData[int(lineSelect)-1] = newTextLine+"\n"
		File.close()
		File = open(str(Filename) + ".txt","w")
		for n in fileLineData:
			File.write(n)
		File.close()

