#Dominik Zimny
#3/12/2019

#Open the test file under the name "file"
#Open in write mode
file = open("test.txt", "w")

#Overwrite the current file with this text
file.write("Sure is")

#Close the file once done with it
file.close()

#Can't read in write mode, and vice versa
#Reopen the file
file = open("test.txt")

#Read the file and print it
print(file.read())

#Close the file again
file.close()
